reccomend: virtualenv/virtualenv-wrapper
			mkvirtualenv yod
			workon yod

pip freeze // to check lib
pip install nose // test suite
pip install rednose // make color in test suite

nosetests --rednose test_fizzbuzz.py // run test