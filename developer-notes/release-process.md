# Pre-release checks #

- `export DEVELOPER_MODE=1`  # good idea to have this always set while developping
- build_cython / build_ext
- check for warnings/errors needing fixing

# Releasing a new version #
 * `export DEVELOPER_MODE=0`  # or just not have it set
 * Bump version in `setup.py`
 * Add release date to `Changes.txt`
 * Check `hg status -u`, if necessary run `hg purge` to avoid undesired files in the tarball.
 * `./setup.py build_cython`
 * `./setup.py sdist`
 * Extract tarball in temporary directory,
    * `python3 setup.py build_ext --inplace && python3 -m pytest test`
    * `python setup.py build_ext --inplace && python -m pytest test`
    * Run tests under valgrind. Build python `--with-valgrind --with-pydebug`, then `valgrind --trace-children=yes "--trace-children-skip=*mount*" python-dbg -m pytest test/`
    * `./setup.py build_sphinx`
    * `./setup.py upload_docs`
    * `./setup.py sdist upload --sign`
 * git commit, git tag -s
