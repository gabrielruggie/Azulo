import typing

class NubeLibraryConstants:

    GOOGLE_CLOUD = "gcloud"

    # Does a simple validation check on syntax and spelling of 
    # user library
    def validate_library (cls, library: str) -> bool:

        if library not in [cls.GOOGLE_CLOUD]:
            return False
        
        return True