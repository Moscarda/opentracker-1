%define debug_package %{nil}

Name:           opentracker
Version:        2012.04.03
Release:        1%{?dist}
Summary:        An open and free bittorrent tracker
Group:          Applications/Internet
License:        Beerware
URL:            http://erdgeist.org/arts/software/opentracker/
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root

%description
Opentracker is a open and free bittorrent tracker project. It aims for minimal resource usage and is intended to run at your wlan router.

A torrent tracker basically is an http-Server that collects all clients ip addresses into pools sorted by one of the request strings parameters and answers all other clients that specified this exact same parameter a list of all other recent clients. All technologies to implement this are around for more than twenty years. Still most implementations suck performancewise.

Utilizing the highly scalable server framework from libowfat, opentracker can easily serve multiple thousands of requests on a standard plastic WLAN-router, limited only by your kernels capabilities ;)

One important design decision of opentracker was to not store any data persistently. This reduces wear&tear on hard disks and eliminates problems with corrupt databases.

%prep
cp -a $RPM_SOURCE_DIR/* .

%build
make

%install
mkdir -p $RPM_BUILD_ROOT%{_bindir}/
cp -a opentracker/opentracker $RPM_BUILD_ROOT%{_bindir}/

%clean
rm -rf $RPM_BUILD_ROOT

%files
%attr(0755,root,root) %{_bindir}/opentracker

