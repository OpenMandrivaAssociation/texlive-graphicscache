Name:		texlive-graphicscache
Version:	60150
Release:	1
Summary:	Cache includegraphics calls
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/graphicscache
License:	bsd3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/graphicscache.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/graphicscache.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/graphicscache.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This LaTeX package provides caching of \includegraphics calls,
with several useful effects: Recompilations are much faster
(10x speedup observed). Images can be postprocessed with
ghostscript before inclusion, thus: Automatic downscaling to
specified DPI Automatic JPEG compression with configurable
quality Much smaller files (e.g. 10MB instead of 150MB)! Note:
Due to the one-by-one invocation of pdflatex and ghostscript
for each graphics element, the first compilation is typically
slower than usual. Note: graphicscache needs the \write18 call
(also called shell escape). This is a security risk if you have
untrusted TeX sources. graphicscache supports pdfLaTeX and
LuaLaTeX; XeLaTeX is not supported.

%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/source/latex/graphicscache
%{_texmfdistdir}/tex/latex/graphicscache
%doc %{_texmfdistdir}/doc/latex/graphicscache

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
