all: bin

bin:
	(cd src && make all) || exit 1
	mkdir -p dist
	cp -a src/opentracker/opentracker dist/

# use rpmbuild to build the source out of the build directory w/o polluting the src directory with build output
rpm:
	rm -rf build
	mkdir -p build/{BUILD,BUILDROOT,RPMS,SOURCES,SPECS,SRPMS} dist
	cp -a src build/SOURCES
	rpmbuild -bb --define "_topdir $(PWD)/build" spec/opentracker.spec
	cp -a build/RPMS/*/*.rpm dist/

clean:
	(cd src && make clean) || exit 1
	rm -rf build dist

