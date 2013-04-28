%define	sver	%(echo %{version} | tr -d .)
Summary:	PHP class which allows to generate PDF files with pure PHP
Summary(pl.UTF-8):	Klasa PHP pozwalająca na generowanie plikow PDF w czystym PHP
Name:		php-fpdf
Version:	1.7
Release:	1
License:	Freeware
Group:		Libraries
Source0:	http://fpdf.org/en/dl.php?v=17&f=tgz?/fpdf%{sver}.tgz
# Source0-md5:	39b27b785695211ab66a36264b149f2b
# http://www.fpdf.de/downloads/addons/69/
Source1:	fpdf-draw.php
# Source1-md5:	cd7711f7b39a0066ac20cb3f535ba973
Source2:	fpdf-verdana.tar.gz
# Source2-md5:	101cd6ae9867ade8cbb12973a35e83f8
URL:		http://www.fpdf.org/
Requires:	php(core)
Obsoletes:	fpdf < 1:1.7-3
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
FPDF is a PHP class which allows to generate PDF files with pure PHP,
that is to say without using the PDFlib library. F from FPDF stands
for Free: you may use it for any kind of usage and modify it to suit
your needs.

%description -l pl.UTF-8
FPDF to klasa PHP pozwalająca na generowanie plików PDF w czystym PHP,
tzn. bez użycia biblioteki PDFlib. F z FPDF oznacza "Free": można jej
używać w dowolny sposób i modyfikować w zależności od potrzeb.

%package doc
Summary:	Documentation for FPDF
Group:		Documentation

%description doc
Documentation for FPDF.

%prep
%setup -q -n fpdf%{sver} -a2

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_data_dir}/fpdf
cp -a fpdf.* font $RPM_BUILD_ROOT%{php_data_dir}/fpdf
cp -p fpdf-verdana/*.* $RPM_BUILD_ROOT%{php_data_dir}/fpdf/font
cp -p %{SOURCE1} $RPM_BUILD_ROOT%{php_data_dir}/fpdf/draw.php

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{php_data_dir}/fpdf

%files doc
%defattr(644,root,root,755)
%doc doc tutorial *.htm *.txt
