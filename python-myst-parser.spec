Summary:	An extended commonmark compliant parser, with bridges to docutils & sphinx
Name:		python-myst-parser
Version:	4.0.0
Release:	1
Group:		Development/Python
License:	MIT
URL:		https://github.com/executablebooks/MyST-Parser
#Source0:	https://github.com/executablebooks/MyST-Parser/archive/%{version}/myst-parser-%{version}.tar.gz
Source0:	https://pypi.io/packages/source/m/myst-parser/myst_parser-%{version}.tar.gz
BuildRequires:	pkgconfig(python)
BuildRequires:	python%{pyver}dist(mdit-py-plugins)
BuildRequires:	python%{pyver}dist(pip)
BuildRequires:	python%{pyver}dist(setuptools)
BuildRequires:	python%{pyver}dist(wheel)

BuildArch:	noarch

%description
MyST is a rich and extensible flavor of Markdown meant for technical
documentation and publishing.

MyST is a flavor of markdown that is designed for simplicity, flexibility,
and extensibility. This repository serves as the reference implementation
of MyST Markdown, as well as a collection of tools to support working with
MyST in Python and Sphinx. It contains an extended CommonMark-compliant parser
using markdown-it-py, as well as a Sphinx extension that allows you to write
MyST Markdown in Sphinx.

%files
%license LICENSE
%doc README.md
%{_bindir}/myst-*
%{py_sitedir}/myst_parser
%{py_sitedir}/myst_parser-*.*-info

#--------------------------------------------------------------------

%prep
%autosetup -n myst_parser-%{version}

%build
%py_build
 
%install
%py_install
