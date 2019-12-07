#
# Conditional build:
%bcond_without	python2	# CPython 2.x module
%bcond_with	python3	# CPython 3.x module [already included in 3.3+ distribution]
%bcond_without	tests	# do not perform "make test"

%define 	module	ipaddress
Summary:	IPv4/IPv6 manipulation library
Summary(pl.UTF-8):	Biblioteka do operacji na adresach IPv4/IPv6
Name:		python-%{module}
Version:	1.0.23
Release:	1
License:	PSF
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/ipaddress/
Source0:	https://files.pythonhosted.org/packages/source/i/ipaddress/%{module}-%{version}.tar.gz
# Source0-md5:	aaee67a8026782af1831148beb0d9060
URL:		https://pypi.org/project/ipaddress/
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
%if %{with python2}
BuildRequires:	python-modules >= 1:2.6
%endif
%if %{with python3}
BuildRequires:	python3-modules >= 1:3.2
BuildRequires:	python3-modules < 1:3.3
%endif
Requires:	python-modules >= 1:2.6
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
IPv4/IPv6 manipulation library.

%description -l pl.UTF-8
Biblioteka do operacji na adresach IPv4/IPv6.

%package -n python3-%{module}
Summary:	IPv4/IPv6 manipulation library
Summary(pl.UTF-8):	Biblioteka do operacji na adresach IPv4/IPv6
Group:		Libraries/Python
Requires:	python-modules >= 1:3.2
Requires:	python-modules < 1:3.3

%description -n python3-%{module}
IPv4/IPv6 manipulation library.

%description -n python3-%{module} -l pl.UTF-8
Biblioteka do operacji na adresach IPv4/IPv6.

%prep
%setup -q -n %{module}-%{version}

%build
%if %{with python2}
%py_build %{?with_tests:test}
%endif

%if %{with python3}
%py3_build %{?with_tests:test}
%endif

%install
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%py_install

%py_postclean
%endif

%if %{with python3}
%py3_install
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%files
%defattr(644,root,root,755)
%doc README.md
%{py_sitescriptdir}/ipaddress.py[co]
%{py_sitescriptdir}/ipaddress-%{version}-py*.egg-info
%endif

%if %{with python3}
%files -n python3-%{module}
%defattr(644,root,root,755)
%doc README.md
%{py3_sitescriptdir}/ipaddress.py
%{py3_sitescriptdir}/__pycache__/ipaddress.cpython-*.py[co]
%{py3_sitescriptdir}/ipaddress-%{version}-py*.egg-info
%endif
