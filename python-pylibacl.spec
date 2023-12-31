

%define 	module	pylibacl

Summary:	A Python module for manipulating POSIX.1e ACLs
Summary(pl):	Modu� j�zyka Python pozwalaj�cy na dost�p do ACL standardu POSIX.1e
Name:		python-%{module}
Version:	0.2.1
Release:	2
License:	GPL
Group:		Libraries/Python
Source0:	http://dl.sourceforge.net/%{module}/%{module}-%{version}.tar.gz
# Source0-md5:	a1c3638fae0630dfa715f9143bd71ad5
URL:		http://pylibacl.sourceforge.net/
BuildRequires:	acl-devel
BuildRequires:	rpm-pythonprov
%pyrequires_eq	python-libs
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A Python module for accessing Extended Attributes of the files.

%description -l pl
Modu� j�zyka Python pozwalaj�cy na dost�p do rozszerzonych atrybut�w
plik�w.

%prep
%setup -q -n %{module}-%{version}

%install
rm -rf $RPM_BUILD_ROOT

python setup.py install \
	--root=$RPM_BUILD_ROOT \
	--optimize=2

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.html
%attr(755,root,root) %{py_sitedir}/*.so
