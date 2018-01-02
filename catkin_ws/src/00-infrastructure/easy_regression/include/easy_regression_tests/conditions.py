from comptests.registrar import comptest, run_module_tests
from easy_regression.conditions.interface import RTParseError
from easy_regression.conditions.references import parse_reference
from easy_regression.conditions.implementation import _parse_regression_test_check


@comptest
def parse_condition_check_good():
    good = [
        'v:analyzer/test/statistic >= 12', 
        'v:analyzer/test/statistic@2016-12-01 <= 2',
        
    ]
    for g in good:
        _parse_regression_test_check(g)
         
    
@comptest
def parse_condition_check_bad():
    bad = [
        'v:analyzer/test',
        'v:analyzer/test/statistic@2016-12-0a',
        'v:analyzer/test/statistic@',
        'v:analyzer/test/statistic~',
        'v:analyzer/test/statistic~@2016-12-01',
    ]
    for b in bad:
        try:
            res = parse_reference(b)
        except RTParseError:
            pass
        else:
            msg = 'Expected DTParseError.'
            msg += '\nString: %r' % b
            msg += '\nReturns: %s' % res
            raise Exception(msg)


if __name__ == '__main__':
    run_module_tests()
