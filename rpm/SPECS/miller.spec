#
# XXX - miller 6 is a rewrite in go
#

Summary: Name-indexed data processing tool
Name: miller
Version: 5.10.4
Release: 7%{?dist}
License: BSD
Source: https://github.com/johnkerl/miller/archive/refs/tags/v%{version}.tar.gz
URL: http://johnkerl.org/miller/doc
BuildRequires: flex >= 2.5.35
BuildRequires: gcc
BuildRequires: make
BuildRequires: musl-static >= 1.2.4-0

%description
Miller (mlr) allows name-indexed data such as CSV and JSON files to be
processed with functions equivalent to sed, awk, cut, join, sort etc. It can
convert between formats, preserves headers when sorting or reversing, and
streams data where possible so its memory requirements stay small. It works
well with pipes and can feed "tail -f".

%prep
%setup -q -n miller-%{version}

%build
. /etc/profile
sed -i 's/-g -pg//g' c/Makefile.am c/Makefile.in
%configure \
  CC="musl-gcc" \
  CFLAGS="-fPIC -Wl,-static" \
  LDFLAGS="-static"
make %{?_smp_mflags}

%check
. /etc/profile
echo make check

%install
. /etc/profile
make DESTDIR=%{buildroot} install-strip

%files
%doc README.md
%{_bindir}/mlr
%{_mandir}/man1/mlr.1*

%changelog
* Thu May 25 2023 ryanwoodsmall
- musl 1.2.4
- source profile

* Fri Apr 29 2022 ryan woodsmall <rwoodsmall@gmail.com>
- release bump for musl 1.2.3

* Wed Mar 24 2021 ryan woodsmall <rwoodsmall@gmail.com>
- 5.10.2 release

* Sun Mar 21 2021 ryan woodsmall <rwoodsmall@gmail.com>
- 5.10.1 release

* Fri Jan 15 2021 ryan woodsmall <rwoodsmall@gmail.com>
- release bump for musl 1.2.2

* Wed Dec 30 2020 ryan woodsmall <rwoodsmall@gmail.com>
- release bump for musl CVE-2020-28928

* Thu Dec 03 2020 ryan woodsmall <rwoodsmall@gmail.com>
- 5.7.0 release
- 5.8.0 release
- 5.9.0 release
- 5.9.1 release
- 5.10.0 release
- disable man page

* Tue Oct 20 2020 ryan woodsmall <rwoodsmall@gmail.com>
- release bump for musl 1.2.1

* Sat Oct 26 2019 ryan woodsmall <rwoodsmall@gmail.com>
- release bump for musl 1.1.24

* Sat Oct 19 2019 ryan woodsmall <rwoodsmall@gmail.com> - 5.6.2-1
- miller 5.6.2

* Thu Sep 12 2019 John Kerl <kerl.john.r@gmail.com> - 5.6.0-1
- 5.6.0 release

* Sat Aug 31 2019 John Kerl <kerl.john.r@gmail.com> - 5.5.0-1
- 5.5.0 release

* Tue May 28 2019 Stephen Kitt <steve@sk2.org> - 5.4.0-1
- Fix up for Fedora

* Sun Oct 14 2018 John Kerl <kerl.john.r@gmail.com> - 5.4.0-1
- 5.4.0 release

* Sat Jan 06 2018 John Kerl <kerl.john.r@gmail.com> - 5.3.0-1
- 5.3.0 release

* Thu Jul 20 2017 John Kerl <kerl.john.r@gmail.com> - 5.2.2-1
- 5.2.2 release

* Mon Jun 19 2017 John Kerl <kerl.john.r@gmail.com> - 5.2.1-1
- 5.2.1 release

* Sun Jun 11 2017 John Kerl <kerl.john.r@gmail.com> - 5.2.0-1
- 5.2.0 release

* Thu Apr 13 2017 John Kerl <kerl.john.r@gmail.com> - 5.1.0-1
- 5.1.0 release

* Sat Mar 11 2017 John Kerl <kerl.john.r@gmail.com> - 5.0.1-1
- 5.0.1 release

* Mon Feb 27 2017 John Kerl <kerl.john.r@gmail.com> - 5.0.0-1
- 5.0.0 release

* Sun Aug 21 2016 John Kerl <kerl.john.r@gmail.com> - 4.5.0-1
- 4.5.0 release

* Mon Apr 04 2016 John Kerl <kerl.john.r@gmail.com> - 3.5.0-1
- 3.5.0 release

* Sun Feb 14 2016 John Kerl <kerl.john.r@gmail.com> - 3.4.0-1
- 3.4.0 release

* Sun Feb 07 2016 John Kerl <kerl.john.r@gmail.com> - 3.3.2-1
- Initial spec-file submission for Miller
