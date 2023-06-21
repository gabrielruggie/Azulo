from interpreter.src.scanners.FileScanner import FileScanner
from interpreter.src.Lexer import Lexer


# Tests lexer's ability to form a dictionary from a valid module block
def test_basic_module_creation ():
    scanner = FileScanner('test01.azlp')
    lexer = Lexer(scanner=scanner)
    result:list = lexer.process()
    assert result[0] == {'type': 'project', 'name': 'my_project', 'budget': '600', 'duration': '31', 'strict': 'false'}

# Tests lexer's ability to ignore header above valid module block
def test_basic_module_header_comments ():
    scanner = FileScanner('test02.azlp')
    lexer = Lexer(scanner=scanner)
    result:list = lexer.process()
    assert result[0] == {'type': 'project', 'name': 'my_project', 'budget': '600', 'duration': '31', 'strict': 'false'}

# Tests lexer's ability to handle inline comments
def test_inline_comment ():
    scanner = FileScanner('test03.azlp')
    lexer = Lexer(scanner=scanner)
    result:list = lexer.process()
    assert result[0] == {'type': 'project', 'name': 'my_project', 'budget': '600', 'duration': '31', 'strict': 'false'}

# Tests lexer's ability to handle multiple inline comments
def test_multiple_inline_comments ():
    scanner = FileScanner('test04.azlp')
    lexer = Lexer(scanner=scanner)
    result:list = lexer.process()
    assert result[0] == {'type': 'project', 'name': 'my_project', 'budget': '600', 'duration': '31', 'strict': 'false'}

# Tests lexer's ability to handle comments above module operations
def test_module_comments ():
    scanner = FileScanner('test05.azlp')
    lexer = Lexer(scanner=scanner)
    result:list = lexer.process()
    assert result[0] == {'type': 'project', 'name': 'my_project', 'budget': '600', 'duration': '31', 'strict': 'false'}

# Tests lexer's ability to handle comment blocks both inside and outsire the module declaration
def test_comment_blocks ():
    scanner = FileScanner('test06.azlp')
    lexer = Lexer(scanner=scanner)
    result: list = lexer.process()
    assert result[0] == {'type': 'project', 'name': 'my_project', 'budget': '600', 'duration': '31', 'strict': 'false'}

# Tests lexer's ability to create multiple modules of different sizes and attributes
def test_multiple_module_creation ():
    scanner = FileScanner('test07.azlp')
    lexer = Lexer(scanner=scanner)
    result: list = lexer.process()
    assert result == [{'type': 'project', 'name': 'my_project', 'budget': '600', 'duration': '31', 'strict': 'false'}, {'type': 'category', 'name': 'groceries', 'budget_allocation': '0.25', 'strict': 'true'}, {'type': 'category', 'name': 'clothes', 'budget_allocation': '0.1', 'strict': 'false'}]

def test_report_creation ():
    scanner = FileScanner('test08.azlp')
    lexer = Lexer(scanner=scanner)
    result: list = lexer.process()

    assert result[0] ==     {
                                'type': 'report', 
                                'name': 'default', 
                                'always_run': 'true', 
                                'actions': [
                                            {'module_type': 'category', 'module_name': 'groceries', 'attribute': 'remaining_budget'}, 
                                            {'module_type': 'category', 'module_name': 'ALL', 'attribute': 'remaining_budget'}, 
                                            {'module_type': 'category', 'module_name': 'ALL', 'attribute': 'allocation_amounts'}, 
                                            {'module_type': 'project', 'module_name': 'this', 'attribute': 'remaining_budget'}, 
                                            {'module_type': 'project', 'module_name': 'this', 'attribute': 'burndown'}
                                            ]
                            }