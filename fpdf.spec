%define	sver	%(echo %{version} | tr -d .)
Summary:	PHP class which allows to generate PDF files with pure PHP
Summary(pl.UTF-8):	Klasa PHP pozwalająca na generowanie plikow PDF w czystym PHP
Name:		fpdf
Version:	1.6
Release:	2
Epoch:		1
License:	Freeware
Group:		Libraries
Source0:	%{name}%{sver}.tgz
# Source0-md5:	41867f01ec457bc753feed4372fdd310
# http://www.fpdf.de/downloads/addons/69/
Source1:	fpdf-draw.php
# Source1-md5:	cd7711f7b39a0066ac20cb3f535ba973
Source2:	%{name}-verdana.tar.gz
URL:		http://www.fpdf.org/
Requires:	php-common
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_phpsharedir	%{_datadir}/php

%description
FPDF is a PHP class which allows to generate PDF files with pure PHP,
that is to say without using the PDFlib library. F from FPDF stands
for Free: you may use it for any kind of usage and modify it to suit
your needs.

%description -l pl.UTF-8
FPDF to klasa PHP pozwalająca na generowanie plików PDF w czystym PHP,
tzn. bez użycia biblioteki PDFlib. F z FPDF oznacza "Free": można jej
używać w dowolny sposób i modyfikować w zależności od potrzeb.

%prep
%setup -q -n %{name}%{sver} -a2

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_phpsharedir}/%{name}

cp -a fpdf.* font $RPM_BUILD_ROOT%{_phpsharedir}/%{name}

install fpdf-verdana/*.* $RPM_BUILD_ROOT%{_phpsharedir}/%{name}/font

install %{SOURCE1} $RPM_BUILD_ROOT%{_phpsharedir}/%{name}/draw.php

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc doc tutorial *.htm *.txt
%{_phpsharedir}/%{name}
