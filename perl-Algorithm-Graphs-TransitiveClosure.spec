%define upstream_name	 Algorithm-Graphs-TransitiveClosure
%define upstream_version 2009110901

Name:		    perl-%{upstream_name}
Version:	    %perl_convert_version %{upstream_version}
Release:	    %mkrel 1

Summary:	    Calculate the transitive closure
License:	    GPL+ or Artistic
Group:		    Development/Perl
URL:            http://search.cpan.org/dist/%{upstream_name}
Source0:        http://www.cpan.org/modules/by-module/Algorithm/%{upstream_name}-%{upstream_version}.tar.gz

%if %{mdkversion} < 1010
Buildrequires:	perl-devel
%endif
BuildRoot:	    %{_tmppath}/%{name}-%{version}-%{release}
BuildArch:	    noarch
Obsoletes: perl-TransitiveClosure <= 1.4
Provides:  perl-TransitiveClosure = %{version}-%{release}

%description
This is an implementation of the well known Floyd-Warshall algorithm.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
%{__make} test

%install
rm -rf %{buildroot}
%makeinstall_std

%clean 
rm -rf %{buildroot}

%files 
%defattr(-,root,root)
%doc Changes
%{perl_vendorlib}/Algorithm
%{_mandir}/*/*

