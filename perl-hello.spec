Name:           perl-hello
Version:        %{version}
Release:        1%{?dist}
Summary:        A Hello World script using JSON module

License:        MIT
URL:            https://github.com/keiichi-hikita/perl-hello-rpm
Source0:        hello.pl

BuildArch:      noarch
Requires:       perl

%description
A simple "Hello, World!" program written in Perl using the JSON CPAN module.

%prep

%build
# cpanm などで必要なCPANモジュールをローカルにインストール
mkdir -p lib
PERL_MM_USE_DEFAULT=1 cpanm -L $PWD --installdeps . || :

%install
mkdir -p %{buildroot}/usr/bin
install -m 0755 %{SOURCE0} %{buildroot}/usr/bin/hello.pl

mkdir -p %{buildroot}/usr/lib/perl5/vendor_perl
cp -r lib/perl5/* %{buildroot}/usr/lib/perl5/vendor_perl/

%files
/usr/bin/hello.pl
/usr/lib/perl5/vendor_perl/*

%changelog
* Thu Jun 19 2025 Your Name <you@example.com> - 1.0.0-1
- Add JSON dependency via cpanm
