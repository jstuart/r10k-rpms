%global gem_name faraday_middleware

Name: rubygem-%{gem_name}
Version: 0.9.2
Release: 1%{?dist}
Summary: Various middleware for Faraday
Group: Development/Languages
License: Internal
URL: https://github.com/lostisland/faraday_middleware
Source0: %{gem_name}-%{version}.gem
Requires: ruby(abi) >= 1.8
Requires: ruby(rubygems) >= 1.3.5
Requires: rubygem(faraday) >= 0.7.4
Requires: rubygem(faraday) < 0.10
BuildRequires: ruby(abi) >= 1.8
BuildRequires: rubygems-devel >= 1.3.5
BuildRequires: ruby 
BuildArch: noarch
Provides: rubygem(%{gem_name}) = %{version}

%description
Various middleware for Faraday.


%package doc
Summary: Documentation for %{name}
Group: Documentation
Requires: %{name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{name}.

%prep
gem unpack %{SOURCE0}

%setup -q -D -T -n  %{gem_name}-%{version}

gem spec %{SOURCE0} -l --ruby > %{gem_name}.gemspec

%build
# Create the gem as gem install only works on a gem file
gem build %{gem_name}.gemspec

# %%gem_install compiles any C extensions and installs the gem into ./%%gem_dir
# by default, so that we can move it into the buildroot in %%install
%gem_install

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/




# Run the test suite
%check
pushd .%{gem_instdir}

popd

%files
%dir %{gem_instdir}
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}
%{gem_instdir}/faraday_middleware.gemspec

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/CHANGELOG.md
%doc %{gem_instdir}/CONTRIBUTING.md
%doc %{gem_instdir}/LICENSE.md
%doc %{gem_instdir}/README.md

%changelog
* Thu Sep 10 2015 James Stuart <software@jstuart.org> - 0.9.2-1
- Version bump to 0.9.2
* Tue Oct 21 2014  <rack@puppet-n01> - 0.9.1-1
- Initial package