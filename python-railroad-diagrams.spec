# Copyright 2024 Wong Hoi Sing Edison <hswong3i@pantarei-design.com>
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

%global debug_package %{nil}

%global source_date_epoch_from_changelog 0

Name: python-railroad-diagrams
Epoch: 100
Version: 2.0.4
Release: 1%{?dist}
BuildArch: noarch
Summary: JS+SVG library for drawing railroad syntax diagrams, like on JSON.org
License: MIT
URL: https://pypi.org/project/railroad-diagrams/#history
Source0: %{name}_%{version}.orig.tar.gz
BuildRequires: fdupes
BuildRequires: python-rpm-macros
BuildRequires: python3-devel
BuildRequires: python3-setuptools

%description
Railroad diagrams are a way of visually representing a grammar in a form
that is more readable than using regular expressions or BNF. They can
easily represent any context-free grammar, and some more powerful
grammars.

%prep
%autosetup -T -c -n %{name}_%{version}-%{release}
tar -zx -f %{S:0} --strip-components=1 -C .

%build
%py3_build

%install
%py3_install
find %{buildroot}%{python3_sitelib} -type f -name '*.pyc' -exec rm -rf {} \;
fdupes -qnrps %{buildroot}%{python3_sitelib}

%check

%if 0%{?suse_version} > 1500
%package -n python%{python3_version_nodots}-railroad-diagrams
Summary: JS+SVG library for drawing railroad syntax diagrams, like on JSON.org
Requires: python3
Provides: python3-railroad-diagrams = %{epoch}:%{version}-%{release}
Provides: python3dist(railroad-diagrams) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}-railroad-diagrams = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}dist(railroad-diagrams) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}-railroad-diagrams = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}dist(railroad-diagrams) = %{epoch}:%{version}-%{release}

%description -n python%{python3_version_nodots}-railroad-diagrams
Railroad diagrams are a way of visually representing a grammar in a form
that is more readable than using regular expressions or BNF. They can
easily represent any context-free grammar, and some more powerful
grammars.

%files -n python%{python3_version_nodots}-railroad-diagrams
%license LICENSE
%{python3_sitelib}/*
%endif

%if !(0%{?suse_version} > 1500)
%package -n python3-railroad-diagrams
Summary: JS+SVG library for drawing railroad syntax diagrams, like on JSON.org
Requires: python3
Provides: python3-railroad-diagrams = %{epoch}:%{version}-%{release}
Provides: python3dist(railroad-diagrams) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}-railroad-diagrams = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}dist(railroad-diagrams) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}-railroad-diagrams = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}dist(railroad-diagrams) = %{epoch}:%{version}-%{release}

%description -n python3-railroad-diagrams
Railroad diagrams are a way of visually representing a grammar in a form
that is more readable than using regular expressions or BNF. They can
easily represent any context-free grammar, and some more powerful
grammars.

%files -n python3-railroad-diagrams
%license LICENSE
%{python3_sitelib}/*
%endif

%changelog
