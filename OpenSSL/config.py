{

	"downloads" : [

		"https://www.openssl.org/source/openssl-1.1.1h.tar.gz",

	],

	"url" : "https://www.openssl.org",

	"license" : "LICENSE",

	"commands" : [

		"./config --prefix={buildDir} -fPIC",
		"make -j {jobs}",
		"make install",

	],

	"manifest" : [

		# The "lib" prefix is correct for all platforms

		"lib/libssl*{sharedLibraryExtension}*",
		"lib/libcrypto*{sharedLibraryExtension}*",

	],

	"platform:osx" : {

		"environment" : {

			"KERNEL_BITS" : "64",

		},

	},

	"platform:windows" : {

		# Python builds it's own OpenSSL that we don't want to conflict with

		"manifest" : [],
		"commands" : [],

	},

}
