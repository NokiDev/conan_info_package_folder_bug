from conans import ConanFile

class MyPackage(ConanFile) :
    name = "MyPackage"
    version = "1.0.0"
    default_user="steve"
    default_channel="devel"
    build_policy="missing"

    settings = {
        "os",
        "compiler",
        "build_type",
        "arch"
    }
    options = {
        "myOption" : [True, False]
    }
    
    default_options = (
        "myOption=False"
    )
    
    exports_sources = "*"
    short_paths = True

    def build(self) :
        print("Building nothing")
        
    def build_id(self):
        print("myOption don't impact the build id")
        self.info_build.options.myOption = 'Any'

    def package(self) :
        if self.options.myOption :
          print("True")
        else:
          print("False")