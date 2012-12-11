%define upstream_name	 Algorithm-Graphs-TransitiveClosure
%define upstream_version 2009110901

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	3

Summary:	Calculate the transitive closure
License:	GPL+ or Artistic
Group:		Development/Perl
URL:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Algorithm/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildArch:	noarch
Obsoletes:	perl-TransitiveClosure <= 1.4
Provides:	perl-TransitiveClosure = %{version}-%{release}

%description
This is an implementation of the well known Floyd-Warshall algorithm.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
%makeinstall_std

%files 
%doc Changes
%{perl_vendorlib}/Algorithm
%{_mandir}/*/*

%changelog
* Sat May 28 2011 Funda Wang <fwang@mandriva.org> 2009110901.0.0-2mdv2011.0
+ Revision: 680446
- mass rebuild

* Tue Nov 10 2009 Jérôme Quelin <jquelin@mandriva.org> 2009110901.0.0-1mdv2011.0
+ Revision: 463917
- update to 2009110901

* Fri Jul 17 2009 Jérôme Quelin <jquelin@mandriva.org> 2009040901.0.0-1mdv2010.0
+ Revision: 396790
- renaming package perl-TransitiveClosure to perl-Algorithm-Graphs-TransitiveClosure
- update to 2009040901
- using %%perl_convert_version
- renamed package to perl-Algorithm-Graphs-TransitiveClosure
- fixed license field

* Thu Jul 31 2008 Thierry Vignaud <tv@mandriva.org> 1.4-9mdv2009.0
+ Revision: 258660
- rebuild

* Thu Jul 24 2008 Thierry Vignaud <tv@mandriva.org> 1.4-8mdv2009.0
+ Revision: 246659
- rebuild

* Fri Dec 21 2007 Olivier Blin <oblin@mandriva.com> 1.4-6mdv2008.1
+ Revision: 136362
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Sun Aug 19 2007 Guillaume Rousse <guillomovitch@mandriva.org> 1.4-6mdv2008.0
+ Revision: 67088
- rebuild

