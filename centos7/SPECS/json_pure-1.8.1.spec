# Generated from json_pure-1.8.1.gem by gem2rpm -*- rpm-spec -*-
%global gem_name json_pure
# here goes nothing
%define _unpackaged_files_terminate_build 0

Name: rubygem-%{gem_name}
Version: 1.8.1
Release: 1%{?dist}
Summary: JSON Implementation for Ruby
Group: Development/Languages
License: Internal
URL: http://flori.github.com/json
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
Requires: ruby(release)
Requires: ruby(rubygems) 
BuildRequires: ruby(release)
BuildRequires: rubygems-devel 
BuildRequires: ruby 
# BuildRequires: rubygem(permutation) 
# BuildRequires: rubygem(sdoc) => 0.3.16
# BuildRequires: rubygem(sdoc) < 0.4
BuildArch: noarch
Provides: rubygem(%{gem_name}) = %{version}

%description
This is a JSON implementation in pure Ruby.


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

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/README.rdoc

%changelog
* Fri Sep 19 2014 root <root@puppet-n01.prod.us.ci.rackspace.net> - 1.8.1-1
- Initial package
