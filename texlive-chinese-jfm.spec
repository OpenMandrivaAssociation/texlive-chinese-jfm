Name:		texlive-chinese-jfm
Version:	57758
Release:	2
Summary:	Luatexja-jfm files for Chinese typesetting
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/chinese-jfm
License:	mit
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/chinese-jfm.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/chinese-jfm.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
ChineseJFM is a series of luatexja-jfm files for better Chinese
typesetting, providing quanjiao, banjiao, and kaiming three
styles and other fancy features. It can be used for both
horizontal and vertical writing mode in Simplified/Traditional
Chinese or Japanese fonts.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/luatex/chinese-jfm
%doc %{_texmfdistdir}/doc/luatex/chinese-jfm

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
