import numpy as np


def swap_rows(M, r_index1, r_index2):
    """
    Swap rows in the given matrix.

    Parameters:
    - matrix (numpy.array): The input matrix to perform row swaps on.
    - row_index_1 (int): Index of the first row to be swapped.
    - row_index_2 (int): Index of the second row to be swapped.

    --Turkish version of docstring--

    Bu fonksiyon verilen matriste satırları değiştirir.

    Parametreler:
    - matrix (numpy.array): Satır değişimleri yapılacak giriş matrisi.
    - row_index_1 (int): Değiştirilecek ilk satırın indeksi.
    - row_index_2 (int): Değiştirilecek ikinci satırın indeksi.
    """

    M = M.copy()
    M[[r_index1, r_index2]] = M[[r_index2, r_index1]]
    return M


def get_index_f_non_zero_column(M, column, start_row):
    """
    Retrieve the index of the first non-zero value in a specified column of the given matrix.

    Parameters:
    - matrix (numpy.array): The input matrix to search for non-zero values.
    - column (int): The index of the column to search.
    - starting_row (int): The starting row index for the search.

    Returns:
    int: The index of the first non-zero value in the specified column, starting from the given row.
                Returns -1 if no non-zero value is found.

    --Turkish version of docstring--

    Verilen matriste belirtilen sütunda ilk sıfır olmayan değerin indeksini alır.

    Parametreler:
    - matrix (numpy.array): Sıfır olmayan değerleri aramak için verilen giriş matrisi.
    - column (int): Aranacak sütunun indeksi.
    - starting_row (int): Aramaya başlamak için verilen satır indeksi.

    Dönüş:
    int: Belirtilen sütunda, verilen satırdan başlayarak ilk sıfır olmayan değerin indeksi.
                    Eğer hiç sıfır olmayan değer bulunamazsa -1 döner.

    """
    column_array = M[start_row:, column]
    for i, value in enumerate(column_array):
        if not np.isclose(value, 0, atol=1e-5):
            index = i + start_row
            return index

    return -1


def get_index_f_non_zero_row(M, row, augmented=False):
    """
    Find the index of the first non-zero value in the specified row of the given matrix.

    Parameters:
    - matrix (numpy.array): The input matrix to search for non-zero values.
    - row (int): The index of the row to search.
    - augmented (bool): Pass this True if you are dealing with an augmented matrix,
                        so it will ignore the constant values (the last column in the augmented matrix).

    Returns:
    int: The index of the first non-zero value in the specified row.
         Returns -1 if no non-zero value is found.

    --Turkish version of docstring--

    Verilen matristeki belirtilen satırın ilk sıfır olmayan değerinin dizinini bulun.

    Parametreler:
    - matrix (numpy.array): Sıfır olmayan değerleri aramak için girdi matrisi.
    - row (int): Aranacak satırın dizini.
    - augmented (bool): Artırılmış bir matrisle uğraşıyorsanız True olarak geçirin,
                        böylece sabit değerleri (artırılmış matrisin son sütunu) yoksayar.

    Dönüşler:
    int: Belirtilen satırdaki ilk sıfır olmayan değerin dizini.
         Eğer hiç sıfır olmayan değer bulunamazsa -1 döner.
    """

    M = M.copy()

    if augmented == True:
        M = M[:, :-1]

    row_array = M[row]
    for i, value in enumerate(row_array):
        if not np.isclose(value, 0, atol=1e-5):
            return i
    return -1