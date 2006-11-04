%define	sver	%(echo %{version} | tr -d .)
Summary:	PHP class which allows to generate PDF files with pure PHP
Summary(pl):	Klasa PHP pozwalaj±ca na generowanie plikow PDF w czystym PHP
Name:		fpdf
Version:	1.53
Release:	1
License:	Freeware
Group:		Libraries
Source0:	%{name}%{sver}.tgz
# Source0-md5:	6106c8d0aba37563b7ca9ccc94bc6c95
# http://www.fpdf.de/downloads/addons/69/
Source1:	fpdf-draw.php
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

%description -l pl
FPDF to klasa PHP pozwalaj±ca na generowanie plików PDF w czystym PHP,
tzn. bez u¿ycia biblioteki PDFlib. F z FPDF oznacza "Free": mo¿na jej
u¿ywaæ w dowolny sposób i modyfikowaæ w zale¿no¶ci od potrzeb.

%prep
%setup  -q -n %{name}%{sver}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_phpsharedir}/%{name}

cp -a fpdf.* font $RPM_BUILD_ROOT%{_phpsharedir}/%{name}
install %{SOURCE1} $RPM_BUILD_ROOT%{_phpsharedir}/%{name}/draw.php

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc doc tutorial *.htm *.txt
%{_phpsharedir}/%{name}
