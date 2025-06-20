Name:           perl-hello
Version:        %{version}
Release:        1%{?dist}
Summary:        A simple hello world Perl script

License:        MIT
BuildArch:      noarch
Requires:       perl(JSON)

%description
This is a sample hello world Perl script that uses JSON module.

%prep

%build

%install
mkdir -p %{buildroot}/usr/local/bin
cp %{_sourcedir}/hello.pl %{buildroot}/usr/local/bin/perl-hello
chmod +x %{buildroot}/usr/local/bin/perl-hello

%files
/usr/local/bin/perl-hello

%changelog
* Thu Jun 20 2025 You keiichi.hikita@gmail.com - %{version}-1
- Initial build