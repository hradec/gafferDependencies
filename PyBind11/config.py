{

	"downloads" : [

		"https://github.com/pybind/pybind11/archive/v2.6.2.tar.gz"

	],

	"url" : "https://pybind11.readthedocs.io",

	"license" : "LICENSE",

	"dependencies" : [ "Python" ],

	"environment" : {

		"PATH" : "{buildDir}/bin:$PATH",
		"LD_LIBRARY_PATH" : "{buildDir}/lib",

	},

	"commands" : [

		"cmake"
		" -G {cmakeGenerator}"
		" -D CMAKE_INSTALL_PREFIX={buildDir} ."
		" -D PYBIND11_TEST=0",
		"make install",

	],

	"manifest" : [

		"include/pybind11",

	],

	"platform:windows" : {

		"environment" : {

			"PATH" : "{buildDir}\\bin;%PATH%"

		},

		# using make instead of nmake causes an error "Makefile:35 missing separator. Stop."
		"commands" : [

			"cmake"
			" -G {cmakeGenerator}"
			" -D CMAKE_INSTALL_PREFIX={buildDir} ."
			" -D PYBIND11_TEST=0",
			"nmake install",

		],

	},

}
