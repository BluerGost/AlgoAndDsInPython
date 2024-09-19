import Algorithms
import ProblemSolving


def main():

    # # Insersion Sort
    # insertionSort = Algorithms.InsertionSort()
    # testList = [5, 6 ,1, 4, -1, -3, 6, 10]
    # insertionSort.Sort(testList)
    # print(testList)

    # # Bucket Sort
    # bucketSort = Algorithms.BucketSort()
    # testList = [0.897, 0.565, 0.656, 0.1234, 0.665, 0.3434]
    # bucketSort.Sort(testList)
    # print(testList)

    # # Top K Frequenent Elements
    # topKFrequentElements = ProblemSolving.TopKFrequentElements()
    # testList = [1,2,2,3,3,3]
    # print(topKFrequentElements.Run(testList, 2))

    # String Encode and Decode
    # testData1 = ["neet","code","love","you"]
    # testData2 = []
    testData3 = [""]

    strEncodeAndDecode = ProblemSolving.StringEncodeAndDecode()
    result = strEncodeAndDecode.Run(testData3)
    print(result)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
