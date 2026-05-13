%define module myst-parser
%define oname myst_parser

Name:		python-myst-parser
Summary:	An extended commonmark compliant parser, with bridges to docutils & sphinx
Version:	5.1.0
Release:	1
Group:		Development/Python
License:	MIT
URL:		https://github.com/executablebooks/MyST-Parser
#Source0:	https://github.com/executablebooks/MyST-Parser/archive/v%%{version}/%%{name}-%%{version}.tar.gz
Source0:	https://pypi.io/packages/source/m/%{module}/%{oname}-%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildSystem:	python
BuildArch:	noarch
BuildRequires:	pkgconfig(python)
BuildRequires:	python%{pyver}dist(flit-core)
BuildRequires:	python%{pyver}dist(pip)
BuildRequires:	python%{pyver}dist(setuptools)
BuildRequires:	python%{pyver}dist(wheel)
BuildRequires:	python%{pyver}dist(docutils)
BuildRequires:	python%{pyver}dist(jinja2)
BuildRequires:	python%{pyver}dist(markdown-it-py)
BuildRequires:	python%{pyver}dist(mdit-py-plugins)
BuildRequires:	python%{pyver}dist(pyyaml)
BuildRequires:	python%{pyver}dist(sphinx)

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
%doc README.md
%{_bindir}/myst-{anchors,docutils-demo,docutils-html,docutils-html5,docutils-latex,docutils-pseudoxml,docutils-xml,inv}
%{python_sitelib}/%{oname}
%{python_sitelib}/%{oname}-%{version}.dist-info
