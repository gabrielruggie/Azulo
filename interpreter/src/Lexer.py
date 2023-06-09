from interpreter.src.exceptions.Exceptions import *

class Lexer:

    def __init__(self, ):
        self.__open_brkt_count: int = 0
        self.__closed_brkt_count: int = 0

        self.__comment_flag: bool = False
        self.__module_flag: bool = False
        self.__details_flag: bool = False

        self.__new_module_details: dict = {}
        self.__file_modules: list = []

        self.__file_line_list = self.scanner.get_split_lines()

        self.__line_num = 0

    def set_file_line_list (self, line_list: list) -> None:
        self.__file_line_list = line_list

    def __keyword_controller (self, word: str, idx: int, line: list) -> None:

        match word:
            
            case "module":
                if not self.__comment_flag:
                    self.__module_flag = True
                    self.__new_module_details["type"] = line[idx+1]

            case "//": self.__comment_flag = not self.__comment_flag

            case other: 
                # Only throw error on random word if not in comment zone
                if not self.__comment_flag:
                    raise UnexpectedTokenException(line_num=self.__line_num, unknown_token=word)
    
    def __bracket_controller (self, word: str, idx: int, line: list) -> None:

        match word:

            case "{": 
                if not self.__comment_flag:
                    if self.__open_brkt_count == self.__closed_brkt_count:
                        # Last keyword in module line is the name of the module. Need to save it
                        self.__new_module_details["name"] = line[idx-1]
                        # Now setting module attributes
                        self.__details_flag = True
                        self.__open_brkt_count += 1
                    else:
                        raise MissingBracketException(type='open', word=word)
            
            case "}": 
                if not self.__comment_flag:
                    if (self.__closed_brkt_count + 1) == self.__open_brkt_count:
                        self.__module_flag = False
                        self.__details_flag = False
                        self.__closed_brkt_count += 1
                    else:
                        raise MissingBracketException(type='closing', word=word)

            case "//": self.__comment_flag = not self.__comment_flag

            case other: 
                # Only throw error on random word if not in comment zone
                if not self.__comment_flag:
                    raise IllegalOperatorException(type='module', operator=word)

    def __module_details_controller (self, line: list) -> None:

        match line[0]:
            
            case "\tset": 
                if not self.__comment_flag:
                    self.__new_module_details[line[1]] == line[2]

            case "\\": self.__comment_flag = not self.__comment_flag

            case "\tget": 
                if not self.__comment_flag:
                    action_data = {
                        "module_type": line[1],
                        "module_name": line[2],
                        "attribute": line[3]
                    }
                    if "actions" not in self.__new_module_details:
                        self.__new_module_details["actions"] = []
                        
                    self.__new_module_details["actions"].append(action_data)

            case other: 
                # Only throw error on random word if not in comment zone
                if not self.__comment_flag:
                    raise IllegalOperatorException(type='detail', operator=line[0])


    def process (self) -> list:

        # Create stack trace through each function 
        try:

            # Used skip over words that are expected but not keywords
            skip_cnt: int = 0

            for file_line in self.__file_line_list:
                self.__line_num += 1
                if not self.__details_flag:

                    for string in file_line:
                        string_idx = file_line.index(string)

                        if self.__module_flag:
                            # Skip over <module_type> <module_name>
                            if skip_cnt == 2:
                                skip_cnt = 0
                                self.__bracket_controller(word=string, idx=string_idx, line=file_line)
                                # Might not need this
                                # break
                            else:
                                skip_cnt += 1

                        else:
                            self.__keyword_controller(word=string, idx=string_idx, line=file_line)

                else:
                    self.__module_details_controller(line=file_line)

            # return module dictionary objects
            return self.__file_modules

        except IndexError as idx_e:
            raise MissingParameterException(line_num=self.__line_num)