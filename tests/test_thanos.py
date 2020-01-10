import os
import pytest
import warnings

from thanos import ThanosGlove as thg


@pytest.fixture(scope="session")
def files_tree(tmpdir_factory):
    base = tmpdir_factory.mktemp("test_dirname")
    for n_time in range(10):
        filename = base.join(f"{n_time}_file.txt")
        open(filename, 'a').close()

    return base


@pytest.mark.parametrize('dirname',(
    "test_1",
    "test_2",
    'test_3',
))
def test_check_dirname_true(tmpdir, dirname):
    tmpdir.mkdir(dirname)
    assert thg.check_dirname(tmpdir) == True


@pytest.mark.parametrize('dirname, filename',(
    ('test_1', 'test_file.txt'),
    ('test_2', 'test_file.txt'),
    ('test_3', 'test_file.txt'),
))
def test_check_dirname_false(tmpdir, dirname, filename):
    p = tmpdir.mkdir(dirname).join(filename)
    open(p, 'a').close()
    assert thg.check_dirname(p) == False


def test_list_of_files_length(files_tree):
    files_length = len(os.listdir(files_tree))
    assert files_length == len(thg.list_of_files(files_tree))


def test_remove_files(files_tree):
    files = thg.list_of_files(files_tree)
    files_length = len(os.listdir(files_tree))
    assert round(files_length / 2) == thg.remove_files(files)
