from Calculator.Addition import addition
from Calculator.Subtraction import subtraction
from Calculator.Multiplication import multiplication
from Calculator.Division import division
from Calculator.Squared import squared


def cochran_sample_size(data, confidenceLevel, confidencelevelZscore, testVaribility):
    DataLength = len(data)
    precision = subtraction(1.00, confidenceLevel)
    zScore = confidencelevelZscore
    p = testVaribility
    recommendation = division(multiplication(squared(zScore), multiplication(p, p)), squared(precision))
    cochran = division(recommendation, addition(1, (division(subtraction(recommendation, 1), DataLength))))

    return cochran

SampleData = [50, 8, 85, 2, 99, 75, 78, 70, 93, 79, 99, 97, 74, 16, 93, 44, 26, 79, 74, 91, 92, 9, 83, 71, 92, 36, 27, 73, 7,
     98, 78, 52, 77, 53, 49, 53, 86, 1, 29, 76, 25, 88, 50, 36, 47, 54, 11, 21, 61, 6, 92, 72, 28, 58, 78, 26, 91,
     16, 72, 51, 50, 45, 23, 7, 70, 68, 22, 64, 58, 24, 66, 71, 86, 8, 47, 78, 93, 87, 78, 43, 34, 63, 47, 77, 30,
     76, 61, 10, 66, 71, 7, 99, 84, 22, 56, 64, 96, 53, 39, 38, 96, 61, 69, 28, 13, 67, 97, 73, 12, 78, 73, 46, 11,
     47, 78, 26, 85, 37, 29, 37, 100, 94, 55, 16, 33, 89, 81, 56, 6, 61, 85, 13, 82, 96, 75, 37, 2, 2, 35, 50, 45,
     13, 1, 62, 100, 48, 10, 94, 65, 3, 4, 97, 18, 30, 7, 35, 38, 38, 97, 54, 71, 95, 8, 49, 26, 44, 1, 69, 11, 56,
     48, 75, 37, 42, 29, 99, 9, 61, 20, 20, 33, 45, 90, 80, 5, 30, 30, 8, 82, 53, 50, 59, 73, 77, 21, 31, 8, 72, 98,
     83, 74, 17, 98, 34, 18, 19, 58, 63, 42, 23, 79, 68, 21, 30, 28, 34, 22, 57, 39, 58, 24, 54, 36, 21, 72, 82, 42,
     78, 60, 57, 94, 9, 88, 98, 18, 74, 75, 100, 11, 10, 74, 18, 54, 83, 97, 79, 41, 93, 22, 13, 17, 64, 85, 57, 63,
     54, 84, 58, 55, 13, 28, 78, 96, 37, 44, 11, 91, 29, 64, 51, 13, 46, 63, 17, 47, 17, 29, 71, 34, 84, 35, 8, 4,
     30, 2, 70, 36, 97, 95, 41, 2, 34, 22, 32, 99, 42, 20, 57, 97, 16, 89, 24, 57, 64, 29, 26, 44, 73, 33, 40, 96,
     44, 39, 27, 48, 72, 13, 72, 93, 5, 71, 40, 77, 99, 97, 32, 3, 1, 72, 64, 26, 48, 70, 1, 35, 6, 10, 45, 9, 70,
     92, 67, 22, 2, 49, 44, 52, 52, 63, 82, 48, 42, 81, 88, 33, 65, 72, 92, 5, 71, 96, 75, 74, 18, 43, 28, 63, 70,
     42, 69, 31, 32, 76, 39, 70, 21, 45, 97, 57, 30, 57, 97, 80, 37, 43, 19, 91, 90, 75, 71, 62, 34, 38, 16, 17, 97,
     92, 83, 2, 96, 49, 64, 95, 25, 85, 12, 99, 67, 66, 47, 80, 92, 37, 16, 58, 30, 29, 60, 5, 61, 96, 37, 62, 56,
     34, 75, 77, 82, 39, 84, 4, 11, 25, 34, 65, 8, 19, 78, 81, 63, 3, 19, 99, 32, 96, 32, 17, 24, 4, 13, 44, 88, 39,
     19, 11, 56, 76, 12, 39, 37, 37, 5, 17, 71, 77, 49, 51, 63, 91, 93, 61, 26, 27, 39, 1, 94, 99, 16, 52, 61, 69,
     37, 74, 41, 50, 82, 66, 68, 39, 69, 95, 4, 100, 90, 87, 76, 35, 66, 26, 86, 30, 42, 74, 18, 74, 27, 30, 7, 98,
     35, 22, 7, 40, 58, 4, 37, 59, 84, 57, 6, 31, 86, 64, 76, 7, 5, 59, 5, 46, 36, 29, 49, 51, 67, 46, 59, 87, 78,
     24, 22, 29, 76, 33, 71, 90, 95, 73, 85, 35, 60, 86, 92, 81, 66, 52, 7, 7, 43, 98, 28, 59, 14, 11, 5, 18, 39, 35,
     47, 69, 92, 11, 54, 97, 44, 21, 67, 12, 63, 89, 69, 44, 15, 23, 82, 15, 74, 55, 47, 86, 8, 40, 77, 32, 68, 8,
     86, 59, 69, 96, 31, 70, 73, 96, 27, 94, 44, 53, 1, 48, 81, 6, 53, 32, 98, 49, 25, 14, 26, 59, 98, 31, 24, 39, 8,
     70, 88, 84, 47, 14, 39, 16, 97, 61, 12, 50, 29, 49, 69, 53, 79, 1, 29, 3, 51, 18, 19, 78, 17, 77, 41, 41, 96,
     40, 63, 79, 73, 86, 15, 82, 8, 24, 12, 91, 9, 31, 59, 6, 15, 30, 58, 20, 44, 32, 63, 35, 91, 47, 46, 27, 1, 3,
     13, 17, 42, 95, 68, 50, 100, 5, 4, 5, 68, 63, 49, 85, 56, 69, 92, 96, 94, 17, 65, 16, 89, 64, 93, 61, 69, 47,
     66, 7, 96, 21, 95, 15, 34, 59, 75, 46, 12, 50, 60, 44, 63, 97, 26, 43, 57, 11, 12, 78, 34, 85, 80, 43, 8, 6, 71,
     96, 32, 65, 92, 11, 18, 11, 32, 98, 75, 24, 47, 69, 63, 49, 62, 31, 80, 76, 31, 28, 79, 12, 62, 39, 99, 69, 17,
     50, 59, 10, 79, 4, 59, 19, 9, 54, 28, 84, 85, 38, 84, 43, 30, 55, 9, 72, 57, 33, 82, 76, 48, 52, 1, 2, 50, 23,
     89, 34, 16, 29, 94, 67, 39, 93, 54, 88, 67, 1, 6, 40, 25, 26, 68, 53, 20, 29, 99, 67, 60, 45, 47, 82, 71, 67,
     87, 94, 82, 48, 43, 45, 4, 80, 4, 12, 85, 1, 26, 62, 4, 46, 20, 21, 25, 18, 93, 37, 66, 94, 13, 78, 59, 36, 88,
     64, 94, 99, 9, 80, 95, 95, 97, 22, 81, 74, 72, 9, 40, 81, 94, 52, 5, 63, 63, 33, 19, 93, 3, 84, 54, 45, 18, 43,
     95, 98, 23, 89, 94, 81, 58, 36, 28, 72, 23, 72, 20, 100, 44, 74, 45, 44, 67, 70, 67, 95, 63, 51, 36, 80, 48, 8,
     60, 6, 87, 52, 10, 93, 52, 82, 43, 71, 28, 67, 12, 2, 88, 29, 63, 88, 10, 69, 13, 7, 35, 30, 44, 55, 29, 7, 23,
     94, 9, 5, 7, 8, 74, 94, 69, 14, 72, 71, 57, 30, 37, 62, 70, 48, 61, 76, 35, 63, 51, 88, 74, 8, 5, 34, 29, 16,
     24, 65, 52, 93, 74, 88, 77, 24, 62, 90, 68, 85, 75, 66, 60, 77, 38, 11, 42, 18, 88, 13, 29, 48, 15, 72, 36, 31,
     83, 37, 50, 99, 81]

Ans = cochran_sample_size(SampleData, .95, 1.96, .5)
print(Ans)