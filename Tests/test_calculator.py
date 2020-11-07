import unittest

from Calculator.Calculator import Calculator
from ParseInputs.ParseInputFiles import ParseInputFiles


class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.calculator = Calculator()
        self.datafile = ParseInputFiles()

    def test_instantiate_calculator(self):
        self.assertIsInstance(self.calculator, Calculator)

    def test_results_property_calculator(self):
        self.assertEqual(self.calculator.result, 0)

    def test_add_method_calculator(self):
        filepath = './Tests/testCSVs/Unit Test Addition.csv'
        file_data = self.datafile.parse(filepath)
        for row in file_data:
            self.assertEqual(self.calculator.add(row['Value 2'], row['Value 1']), int(row['Result']))
        file_data.clear()

    def test_subtraction_method_calculator(self):
        filepath = './Tests/testCSVs/Unit Test Subtraction.csv'
        file_data = self.datafile.parse(filepath)
        for row in file_data:
            self.assertEqual(self.calculator.subtract(row['Value 2'], row['Value 1']), int(row['Result']))
        file_data.clear()

    def test_multiplication_method_calculator(self):
        filepath = './Tests/testCSVs/Unit Test Multiplication.csv'
        file_data = self.datafile.parse(filepath)
        for row in file_data:
            self.assertEqual(self.calculator.multiply(row['Value 2'], row['Value 1']), int(row['Result']))
        file_data.clear()

    def test_division_method_calculator(self):
        filepath = './Tests/testCSVs/Unit Test Division.csv'
        file_data = self.datafile.parse(filepath)
        # Test divide by 0
        # self.assertEqual(self.calculator.divide(5, 0), 1)
        # Test CSV Data
        for row in file_data:
            self.assertEqual(self.calculator.divide(row['Value 2'], row['Value 1']), float(row['Result']))
        file_data.clear()

    def test_squared_method_calculator(self):
        filepath = './Tests/testCSVs/Unit Test Square.csv'
        file_data = self.datafile.parse(filepath)
        for row in file_data:
            self.assertEqual(self.calculator.square(row['Value 1']), int(row['Result']))
        file_data.clear()

    def test_root_method_calculator(self):
        filepath = './Tests/testCSVs/Unit Test Square Root.csv'
        file_data = self.datafile.parse(filepath)
        for row in file_data:
            self.assertEqual(round(self.calculator.root(row['Value 1']), 8), round(float(row['Result']), 8))
        file_data.clear()

    def test_mean_method_calculator(self):
        datalist = [2, 5, 7, 10]
        self.assertEqual(self.calculator.mean(datalist), 6)
        datalist.clear()

    def test_median_method_calculator(self):
        datalist = [4, 5, 7, 10]
        self.assertEqual(self.calculator.median(datalist), 6)
        datalist.clear()

    def test_mode_method_calculator(self):
        datalist = [4, 5, 5, 7, 10]
        self.assertEqual(self.calculator.median(datalist), 5)
        datalist.clear()

    def test_variance_method_calculator(self):
        datalist = [-14.82381293, -0.29423447, -13.56067979, -1.6288903, -0.31632439, 0.53459687, -1.34069996,
                    -1.61042692, -4.03220519, -0.24332097]
        self.assertEqual(self.calculator.variance(datalist), 28.822364260579157)
        datalist.clear()

    def test_stddev_method_calculator(self):
        datalist = [-14.82381293, -0.29423447, -13.56067979, -1.6288903, -0.31632439, 0.53459687, -1.34069996,
                    -1.61042692, -4.03220519, -0.24332097]
        self.assertEqual(self.calculator.stddev(datalist), 5.36864640860051)
        datalist.clear()

    def test_zscore_method_calculator(self):
        datalist = [-14.82381293, -0.29423447, -13.56067979, -1.6288903, -0.31632439, 0.53459687, -1.34069996,
                    -1.61042692, -4.03220519, -0.24332097]
        testresults = [-2.0661098311914157, 0.640266665633516, -1.8308302013062225, 0.39166474097297277,
                       0.6361520493375699, 0.7946503364731938, 0.4453450018928058, 0.39510385366447387,
                       -0.055992770266716466, 0.6497501547898212]
        self.assertEqual(self.calculator.zscore(datalist), testresults)
        datalist.clear()


if __name__ == '__main__':
    unittest.main()
