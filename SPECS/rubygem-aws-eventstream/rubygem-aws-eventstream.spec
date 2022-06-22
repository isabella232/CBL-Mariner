%global debug_package %{nil}
%global gem_name aws-eventstream
Summary:        Amazon Web Services event stream library
Name:           rubygem-%{gem_name}
Version:        1.2.0
Release:        1%{?dist}
License:        Apache 2.0
Vendor:         Microsoft Corporation
Distribution:   Mariner
Group:          Development/Languages
URL:            https://github.com/aws/aws-sdk-ruby
# To recreate the tar.gz run the following
#  sudo git clone git@github.com:aws/aws-sdk-ruby.git
#  cd gems/%{gem_name}
#  sudo mv %{gem_name} %{gem_name}-%{version} (find version from the VERSION file)
#  sudo tar -cvf %{gem_name}-%{version}.tar.gz %{gem_name}-%{version}/
Source0:        %{gem_name}-%{version}.tar.gz
BuildRequires:  ruby
Provides:       rubygem(%{gem_name}) = %{version}-%{release}

%description
Amazon Web Services event stream library.

%prep
%setup -q -n %{gem_name}-%{version}

%build
gem build %{gem_name}

%install
gem install -V --local --force --install-dir %{buildroot}/%{gemdir} %{gem_name}-%{version}.gem

%files
%defattr(-,root,root,-)
%{gemdir}

%changelog
* Wed Jun 22 2022 Neha Agarwal <nehaagarwal@microsoft.com> - 1.2.0-1
- Update to v1.2.0.
- Build from .tar.gz source.

* Tue Jan 05 2021 Henry Li <lihl@microsoft.com> - 1.1.0-1
- License verified
- Original version for CBL-Mariner
