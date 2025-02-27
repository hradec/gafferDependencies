{

	"publicVariables" : {

		"pythonIncludeDir" : "{buildDir}/include/python{pythonABIVersion}",
		"pythonLibDir" : "{buildDir}/lib",

	},

	"variants" : [ "2", "3" ],

	"url" : "https://www.python.org",

	"license" : "LICENSE",

	"dependencies" : [ "OpenSSL", "LibFFI" ],

	"environment" : {

		"LDFLAGS" : "-L{buildDir}/lib",
		"CPPFLAGS" : "-I{buildDir}/include",
		"LD_LIBRARY_PATH" : "{buildDir}/lib",

	},

	"commands" : [

		"./configure --prefix={buildDir} {libraryType} --enable-unicode=ucs4 --with-ensurepip=install --with-system-ffi",
		"make -j {jobs}",
		"make install",

	],

	"manifest" : [

		"bin/python{executableExtension}",
		"bin/python*[0-9]{executableExtension}",

		"include/python*",

		"lib/{libraryPrefix}python*{sharedLibraryExtension}*",
		"lib/Python.framework*",
		"lib/python{pythonVersion}",

	],

	"variables" : {

		"libraryType" : "--enable-shared",

	},

	"variant:2" : {

		"downloads" : [

			"https://www.python.org/ftp/python/2.7.15/Python-2.7.15.tgz",

		],

		"publicVariables" : {

			"pythonVersion" : "2.7",
			"pythonABIVersion" : "2.7",
			"pythonMajorVersion" : "2",
			"pythonMinorVersion" : "7",

		},

	},

	"variant:3" : {

		"downloads" : [

			"https://www.python.org/ftp/python/3.7.6/Python-3.7.6.tgz",

		],

		"publicVariables" : {

			"pythonVersion" : "3.7",
			# On POSIX systems, Python 3 unconditionally puts these infuriating "m" ABI 
			# suffixes on everything. This is intended to allow different types of Python 
			# builds to exist in the same place, but that's not a problem we have. The 
			# problem we _do_ have is that a bunch of our projects get tripped up by these
			# suffixes. See : https://www.python.org/dev/peps/pep-3149.
			"pythonABIVersion" : "3.7m",
			"pythonMajorVersion" : "3",
			"pythonMinorVersion" : "7",

		},

	},

	"platform:linux" : {

		"variant:3" : {

			"symbolicLinks" : [

				( "{buildDir}/bin/python", "python3" ),

			],

		}

	},

	"platform:osx" : {

		"variables" : {

			"libraryType" : "--enable-framework={buildDir}/lib",

		},

		"publicVariables" : {

			"pythonIncludeDir" : "{buildDir}/lib/Python.framework/Headers",
			"pythonLibDir" : "{buildDir}/lib/Python.framework/Versions/{pythonVersion}/lib",

		},

		"symbolicLinks" : [

			( "{buildDir}/bin/python", "../lib/Python.framework/Versions/Current/bin/python{pythonMajorVersion}" ),
			( "{buildDir}/bin/python{pythonMajorVersion}", "../lib/Python.framework/Versions/Current/bin/python{pythonMajorVersion}" ),
			( "{buildDir}/bin/python{pythonVersion}", "../lib/Python.framework/Versions/Current/bin/python{pythonVersion}" ),
			( "{buildDir}/lib/Python.framework/Versions/Current/lib/libpython{pythonMajorVersion}.dylib", "libpython{pythonMajorVersion}.{pythonMinorVersion}.dylib" ),
		],

	},

	"platform:windows" : {

		"publicVariables" : {

			"pythonIncludeDir" : "{buildDirFwd}/include",
			"pythonLibDir" : "{buildDirFwd}/libs",

		},

		"manifest" : [

			"bin/python{executableExtension}",
			"bin/{libraryPrefix}python*{sharedLibraryExtension}*",

			"lib/{libraryPrefix}python*.lib",
			"lib/python{pythonVersion}",

			"libs",

			"DLLs",

			# Gross. But here's the reasoning for now: we can't put the modules into a directory
			# like `lib` as on Linux because it causes havoc with cmake finding the site-packages
			# directory for downstream projects that need to install their Python modules.
			# If we just do `Lib/*` then the packager will sweep up everything in the `lib`
			# folder at the end of the entire dependencies build, not at the time Python is built.
			# So for now to come up with this list, do a build of just Python, and then a simple
			# Python script or similar to get a list of everything in the `lib` folder.
			"Lib/abc.py",
			"Lib/aifc.py",
			"Lib/antigravity.py",
			"Lib/argparse.py",
			"Lib/ast.py",
			"Lib/asynchat.py",
			"Lib/asyncio",
			"Lib/asyncore.py",
			"Lib/base64.py",
			"Lib/bdb.py",
			"Lib/binhex.py",
			"Lib/bisect.py",
			"Lib/bz2.py",
			"Lib/calendar.py",
			"Lib/cgi.py",
			"Lib/cgitb.py",
			"Lib/chunk.py",
			"Lib/cmd.py",
			"Lib/code.py",
			"Lib/codecs.py",
			"Lib/codeop.py",
			"Lib/collections",
			"Lib/colorsys.py",
			"Lib/compileall.py",
			"Lib/concurrent",
			"Lib/configparser.py",
			"Lib/contextlib.py",
			"Lib/contextvars.py",
			"Lib/copy.py",
			"Lib/copyreg.py",
			"Lib/cProfile.py",
			"Lib/crypt.py",
			"Lib/csv.py",
			"Lib/ctypes",
			"Lib/curses",
			"Lib/dataclasses.py",
			"Lib/datetime.py",
			"Lib/dbm",
			"Lib/decimal.py",
			"Lib/difflib.py",
			"Lib/dis.py",
			"Lib/distutils",
			"Lib/doctest.py",
			"Lib/dummy_threading.py",
			"Lib/email",
			"Lib/encodings",
			"Lib/enum.py",
			"Lib/filecmp.py",
			"Lib/fileinput.py",
			"Lib/fnmatch.py",
			"Lib/formatter.py",
			"Lib/fractions.py",
			"Lib/ftplib.py",
			"Lib/functools.py",
			"Lib/genericpath.py",
			"Lib/getopt.py",
			"Lib/getpass.py",
			"Lib/gettext.py",
			"Lib/glob.py",
			"Lib/gzip.py",
			"Lib/hashlib.py",
			"Lib/heapq.py",
			"Lib/hmac.py",
			"Lib/html",
			"Lib/http",
			"Lib/imaplib.py",
			"Lib/imghdr.py",
			"Lib/imp.py",
			"Lib/importlib",
			"Lib/inspect.py",
			"Lib/io.py",
			"Lib/ipaddress.py",
			"Lib/json",
			"Lib/keyword.py",
			"Lib/lib2to3",
			"Lib/linecache.py",
			"Lib/locale.py",
			"Lib/logging",
			"Lib/lzma.py",
			"Lib/macpath.py",
			"Lib/mailbox.py",
			"Lib/mailcap.py",
			"Lib/mimetypes.py",
			"Lib/modulefinder.py",
			"Lib/msilib",
			"Lib/multiprocessing",
			"Lib/netrc.py",
			"Lib/nntplib.py",
			"Lib/ntpath.py",
			"Lib/nturl2path.py",
			"Lib/numbers.py",
			"Lib/opcode.py",
			"Lib/operator.py",
			"Lib/optparse.py",
			"Lib/os.py",
			"Lib/pathlib.py",
			"Lib/pdb.py",
			"Lib/pickle.py",
			"Lib/pickletools.py",
			"Lib/pipes.py",
			"Lib/pkgutil.py",
			"Lib/platform.py",
			"Lib/plistlib.py",
			"Lib/poplib.py",
			"Lib/posixpath.py",
			"Lib/pprint.py",
			"Lib/profile.py",
			"Lib/pstats.py",
			"Lib/pty.py",
			"Lib/pyclbr.py",
			"Lib/pydoc.py",
			"Lib/pydoc_data",
			"Lib/py_compile.py",
			"Lib/queue.py",
			"Lib/quopri.py",
			"Lib/random.py",
			"Lib/re.py",
			"Lib/reprlib.py",
			"Lib/rlcompleter.py",
			"Lib/runpy.py",
			"Lib/sched.py",
			"Lib/secrets.py",
			"Lib/selectors.py",
			"Lib/shelve.py",
			"Lib/shlex.py",
			"Lib/shutil.py",
			"Lib/signal.py",
			"Lib/site-packages",
			"Lib/site.py",
			"Lib/smtpd.py",
			"Lib/smtplib.py",
			"Lib/sndhdr.py",
			"Lib/socket.py",
			"Lib/socketserver.py",
			"Lib/sqlite3",
			"Lib/sre_compile.py",
			"Lib/sre_constants.py",
			"Lib/sre_parse.py",
			"Lib/ssl.py",
			"Lib/stat.py",
			"Lib/statistics.py",
			"Lib/string.py",
			"Lib/stringprep.py",
			"Lib/struct.py",
			"Lib/subprocess.py",
			"Lib/sunau.py",
			"Lib/symbol.py",
			"Lib/symtable.py",
			"Lib/sysconfig.py",
			"Lib/tabnanny.py",
			"Lib/tarfile.py",
			"Lib/telnetlib.py",
			"Lib/tempfile.py",
			"Lib/textwrap.py",
			"Lib/this.py",
			"Lib/threading.py",
			"Lib/timeit.py",
			"Lib/token.py",
			"Lib/tokenize.py",
			"Lib/trace.py",
			"Lib/traceback.py",
			"Lib/tracemalloc.py",
			"Lib/tty.py",
			"Lib/types.py",
			"Lib/typing.py",
			"Lib/unittest",
			"Lib/urllib",
			"Lib/uu.py",
			"Lib/uuid.py",
			"Lib/warnings.py",
			"Lib/wave.py",
			"Lib/weakref.py",
			"Lib/webbrowser.py",
			"Lib/wsgiref",
			"Lib/xdrlib.py",
			"Lib/xml",
			"Lib/xmlrpc",
			"Lib/zipapp.py",
			"Lib/zipfile.py",
			"Lib/_bootlocale.py",
			"Lib/_collections_abc.py",
			"Lib/_compat_pickle.py",
			"Lib/_compression.py",
			"Lib/_dummy_thread.py",
			"Lib/_markupbase.py",
			"Lib/_osx_support.py",
			"Lib/_pydecimal.py",
			"Lib/_pyio.py",
			"Lib/_py_abc.py",
			"Lib/_sitebuiltins.py",
			"Lib/_strptime.py",
			"Lib/_threading_local.py",
			"Lib/_weakrefset.py",
			"Lib/__future__.py",
			"Lib/__phello__.foo.py",
			"Lib/__pycache__",

			# Double gross. Python on Windows seems pretty insistent on having the
			# includes in the `include` directory, not a subdirectory. Many of the
			# GafferDependencies projects can handle it in a subdirectory, but
			# PySide and perhaps others can't. There's also a good change putting
			# includes in a subdirectory would break installing things with pip
			# or setuptools (the distutils.sysconfig.get_config_var("INCLUDEPY") will
			# return the wrong value if the includes are located anywhere except `include`)
			"include/abstract.h",
			"include/accu.h",
			"include/asdl.h",
			"include/ast.h",
			"include/bitset.h",
			"include/bltinmodule.h",
			"include/boolobject.h",
			"include/bytearrayobject.h",
			"include/bytesobject.h",
			"include/bytes_methods.h",
			"include/cellobject.h",
			"include/ceval.h",
			"include/classobject.h",
			"include/code.h",
			"include/codecs.h",
			"include/compile.h",
			"include/complexobject.h",
			"include/context.h",
			"include/datetime.h",
			"include/descrobject.h",
			"include/dictobject.h",
			"include/dtoa.h",
			"include/dynamic_annotations.h",
			"include/enumobject.h",
			"include/errcode.h",
			"include/eval.h",
			"include/fileobject.h",
			"include/fileutils.h",
			"include/floatobject.h",
			"include/frameobject.h",
			"include/funcobject.h",
			"include/genobject.h",
			"include/graminit.h",
			"include/grammar.h",
			"include/import.h",
			"include/intrcheck.h",
			"include/iterobject.h",
			"include/listobject.h",
			"include/longintrepr.h",
			"include/longobject.h",
			"include/marshal.h",
			"include/memoryobject.h",
			"include/metagrammar.h",
			"include/methodobject.h",
			"include/modsupport.h",
			"include/moduleobject.h",
			"include/namespaceobject.h",
			"include/node.h",
			"include/object.h",
			"include/objimpl.h",
			"include/odictobject.h",
			"include/opcode.h",
			"include/osdefs.h",
			"include/osmodule.h",
			"include/parsetok.h",
			"include/patchlevel.h",
			"include/pgen.h",
			"include/pgenheaders.h",
			"include/pyarena.h",
			"include/pyatomic.h",
			"include/pycapsule.h",
			"include/pyconfig.h",
			"include/pyctype.h",
			"include/pydebug.h",
			"include/pydtrace.h",
			"include/pyerrors.h",
			"include/pyexpat.h",
			"include/pyfpe.h",
			"include/pyhash.h",
			"include/pylifecycle.h",
			"include/pymacconfig.h",
			"include/pymacro.h",
			"include/pymath.h",
			"include/pymem.h",
			"include/pyport.h",
			"include/pystate.h",
			"include/pystrcmp.h",
			"include/pystrhex.h",
			"include/pystrtod.h",
			"include/Python-ast.h",
			"include/Python.h",
			"include/pythonrun.h",
			"include/pythread.h",
			"include/pytime.h",
			"include/py_curses.h",
			"include/rangeobject.h",
			"include/setobject.h",
			"include/sliceobject.h",
			"include/structmember.h",
			"include/structseq.h",
			"include/symtable.h",
			"include/sysmodule.h",
			"include/token.h",
			"include/traceback.h",
			"include/tupleobject.h",
			"include/typeslots.h",
			"include/ucnhash.h",
			"include/unicodeobject.h",
			"include/warnings.h",
			"include/weakrefobject.h",

			# `lib` prefix is correct for Windows
			"DLLs/libssl*{sharedLibraryExtension}*",
			"DLLs/libcrypto*{sharedLibraryExtension}*",
		],

		"commands" : [

			"call PCbuild/build.bat -p x64 --no-tkinter",

			# Recreate the typical Python 3 directory structure
			"if not exist {buildDir}\\DLLs mkdir {buildDir}\\DLLs",
			"if not exist {buildDir}\\bin mkdir {buildDir}\\bin",
			"if not exist {buildDir}\\lib mkdir {buildDir}\\lib",
			"if exist {buildDir}\\libs rmdir /Q /S {buildDir}\\libs",
			"if not exist {buildDir}\\include mkdir {buildDir}\\include",
			"if exist {buildDir}\\include\\openssl rmdir /S /Q {buildDir}\\include\\openssl",
			"mkdir {buildDir}\\include\\openssl",

			# Initially copy all components to `DLLs` to avoid needing to copy
			# individual DLL files later
			"PCbuild\\amd64\\python.exe PC\\layout -s . -b PCbuild\\amd64 -v --precompile --flat-dlls --include-pip --include-dev --copy {buildDir}\\DLLs",

			"xcopy /sehyi {buildDir}\\DLLs\\include {buildDir}\\include",
			"xcopy /sehyi {buildDir}\\DLLs\\Lib {buildDir}\\lib",
			"move {buildDir}\\DLLs\\libs {buildDir}",

			"rmdir /Q /S {buildDir}\\DLLs\\include",
			"rmdir /Q /S {buildDir}\\DLLs\\Lib",

			"move {buildDir}\\DLLs\\python.exe {buildDir}\\bin",
			"move {buildDir}\\DLLs\\python{pythonMajorVersion}{pythonMinorVersion}.dll {buildDir}\\bin",
			# pythonw runs a script without an accompanying terminal which means we don't get
			# stdout, stderr, etc.
			"del {buildDir}\\DLLs\\pythonw.exe",
			"del {buildDir}\\DLLs\\LICENSE.txt",  # build.py puts the license in the right place

			# Grab OpenSSL libs from the Python externals (needed by PySide2)
			"copy externals\\openssl-bin-1.1.1d\\amd64\\libcrypto.lib {buildDir}\\lib",
			"copy externals\\openssl-bin-1.1.1d\\amd64\\libssl.lib {buildDir}\\lib",
			"xcopy /sehyi externals\\openssl-bin-1.1.1d\\amd64\\include\\openssl\\* {buildDir}\\include\\openssl",


		],

	}

}
