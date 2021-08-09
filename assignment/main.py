from assignment.manager import save_data


def main():
    flag = 1
    while flag == 1:
        check = save_data()
        print("Please select one of the below option")
        print("1. Run a query")
        print("2. Run the whole process")
        T = int(input())
        if T != 1 and T != 2:
            print("Please select one of the below option")
            print("1. Run a query")
            print("2. Run the whole process")
        if T == 2:
            create_table = input("Want to create table(Y/N)?\n")
            while create_table.upper() != 'Y' and create_table.upper() != 'N':
                create_table = input("Please press Y or N")
            if create_table.upper() == 'Y':
                check.create_table()
                print("TABLE NAME: PRODUCT\nCOLUMNS = NAME, SKU, DESCRIPTION")
            data = input("Please give detailed fine name(file_location/file_name)\n")
            check.save_data_using_parallel_ingestion(data)
            crate_product_count_table = input("want to created a table and check product by name and count?(Y/N)\n")
            if crate_product_count_table.upper() == 'Y':
                check.create_view()
                print("TABLE CREATED")
                print("TABLE NAME: PRODUCT_COUNT\n COLUMNS = NAME, COUNT_OF_PRODUCTS\n")
        print("Write a query\n")
        query = input()
        check.check(query)
        again = input("Want to try again?(Y/N)\n")
        if again.upper() != 'Y':
            flag = 0


if __name__ == '__main__':
    main()