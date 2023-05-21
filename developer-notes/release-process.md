# Pre-release checks #

- `export DEVELOPER_MODE=1`  # good idea to have this always set while developping
- build_cython / build_ext
- check for warnings/errors needing fixing

# Releasing a new version #
 * `export DEVELOPER_MODE=0`  # or just not have it set
 * Bump version in `setup.py` and version/release in `rst/conf.py`
 * Add release date to `Changes.rst`
 * Check `git status` to avoid undesired files in the tarball.
 * `./setup.py build_cython`
 * `./setup.py sdist`
 * Extract tarball in temporary directory,
    * `./setup.py build_ext --inplace && python3 -m pytest test`
    * Run tests under valgrind. Build python `--with-valgrind --with-pydebug`, then `valgrind --trace-children=yes "--trace-children-skip=*mount*" python-dbg -m pytest test/`
    * `sphinx-build -b html rst doc/html`
 * `./util/sdist-sign 1.2.3`  # use real version number, have GPG ready
 * `./util/upload-pypi 1.2.3`  # use real version number, have twine installed
 * git commit, git tag -s
