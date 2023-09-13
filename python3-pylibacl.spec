%define		module	pylibacl
Summary:	A Python module for manipulating POSIX.1e ACLs
Summary(pl.UTF-8):	Moduł języka Python pozwalający na dostęp do ACL standardu POSIX.1e
Name:		python3-%{module}
Version:	0.7.0
Release:	0.1
License:	GPL
Group:		Libraries/Python
Source0:	https://files.pythonhosted.org/packages/source/p/%{module}/%{module}-%{version}.tar.gz
# Source0-md5:	01581ef47c033146a7d06b3014896c59
URL:		https://pylibacl.k1024.org/
BuildRequires:	rpmbuild(macros) >= 1.710
BuildRequires:	acl-devel
BuildRequires:	python3-devel >= 1:3.7
BuildRequires:	rpm-pythonprov
%pyrequires_eq	python3-libs
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A Python module for accessing Extended Attributes of the files.

%description -l pl.UTF-8
Moduł języka Python pozwalający na dostęp do rozszerzonych atrybutów
plików.

%prep
%setup -q -n %{module}-%{version}
%py3_build

%install
rm -rf $RPM_BUILD_ROOT

%py3_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc NEWS.md README.md SECURITY.md
%attr(755,root,root) %{py3_sitedir}/*.so
%{py3_sitedir}/*.egg-info
