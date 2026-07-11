%global tl_name graphicscache
%global tl_revision 65318

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.4
Release:	%{tl_revision}.1
Summary:	Cache includegraphics calls
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/graphicscache
License:	bsd3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/graphicscache.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/graphicscache.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/graphicscache.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This LaTeX package provides caching of \includegraphics calls, with
several useful effects: Recompilations are much faster (10x speedup
observed). Images can be postprocessed with ghostscript before
inclusion, thus: Automatic downscaling to specified DPI Automatic JPEG
compression with configurable quality Much smaller files (e.g. 10MB
instead of 150MB)! Note: Due to the one-by-one invocation of pdflatex
and ghostscript for each graphics element, the first compilation is
typically slower than usual. Note: graphicscache needs the \write18 call
(also called shell escape). This is a security risk if you have
untrusted TeX sources. graphicscache supports pdfLaTeX and LuaLaTeX;
XeLaTeX is not supported.

