
{

	"downloads" : [

		"https://files.pythonhosted.org/packages/21/9f/b251f7f8a76dec1d6651be194dfba8fb8d7781d10ab3987190de8391d08e/six-1.14.0.tar.gz",

	],

	"url" : "https://github.com/benjaminp/six",

	"license" : "LICENSE",

	"commands" : [

		"mkdir -p {buildDir}/python",
		"cp six.py {buildDir}/python",

	],

	"manifest" : [

		"{buildDir}/python/six.py"

	],

	"platform:windows" : {

		"commands" : [
			
			"if not exist {buildDir}\\python mkdir {buildDir}\\python",
			"copy six.py {buildDir}\\python",

		],
		
	},

}
