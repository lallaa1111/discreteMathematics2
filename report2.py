# ========== 1. 관계 행렬 입력 기능 ==========
def input_matrix():
    matrix = []
    # 사용자로부터 5 X 5 크기의 정방행렬을 행 단위로 입력받음
    for i in range(5):
        while True:
            row = list(map(int, input(f"{i + 1}행: ").split()))

            if len(row) != 5:
                print("5개의 원소를 입력하세요.")
                continue

            if any(x not in (0, 1) for x in row):
                print("0 또는 1만 입력하세요.")
                continue

            # 입력 데이터는 리스트(2차원 배열)로 저장
            matrix.append(row)
            break
    return matrix

# ========== 2. 동치 관계 판별 기능 ==========
# 반사 관계 판별
def is_reflexive(matrix):
    for i in range(5):
        if matrix[i][i] != 1:
            return False
    return True

# 대칭 관계 판별
def is_symmetric(matrix):
    for i in range(5):
        for j in range(5):
            if matrix[i][j] != matrix[j][i]:
                return False
    return True

# 추이 관계 판별
def is_transitive(matrix):
    for i in range(5):
        for j in range(5):
            for k in range(5):
                if (matrix[i][j] == 1 and matrix[j][k] == 1 and matrix[i][k] == 0):
                    return False
    return True

# 관계의 성질 판별 결과 및 동치 관계 여부 메시지
def is_equivalence(matrix):
    reflexive = is_reflexive(matrix)
    symmetric = is_symmetric(matrix)
    transitive = is_transitive(matrix)

    print("반사 관계 여부:", reflexive)
    print("대칭 관계 여부:", symmetric)
    print("추이 관계 여부:", transitive)

    if reflexive and symmetric and transitive:
        print("동치 관계입니다.")
        return True

    print("동치 관계가 아닙니다.")
    return False

# ========== 3. 동치 관계일 경우 동치류 출력 기능 ===========
def print_equivalence_classes(matrix):
    for i in range(5):
        equivalence_class = set()

        for j in range(5):
            if matrix[i][j] == 1:
                equivalence_class.add(j + 1)

        print(f"[{i + 1}] = {sorted(equivalence_class)}")

# ========== 4. 폐포 구현 기능 ==========
# 반사 폐포
def reflexive_closure(matrix):
    result = [row[:] for row in matrix]

    for i in range(5):
        result[i][i] = 1

    return result

# 대칭 폐포
def symmetric_closure(matrix):
    result = [row[:] for row in matrix]

    for i in range(5):
        for j in range(5):
            if matrix[i][j] == 1:
                result[j][i] = 1

    return result

# 추이 폐포
def transitive_closure(matrix):
    result = [row[:] for row in matrix]

    for k in range(5):
        for i in range(5):
            for j in range(5):
                if result[i][k] == 1 and result[k][j] == 1:
                    result[i][j] = 1

    return result

# 5. 추가 기능: 폐포 생성 시 추가된 순서쌍 출력
def print_added_pairs(original, closure):
    added = []

    for i in range(5):
        for j in range(5):
            if original[i][j] == 0 and closure[i][j] == 1:
                added.append((i + 1, j + 1))

    print()
    print("추가된 순서쌍: ")
    if added:
        for pair in added:
            print(pair)
    else:
        print("없음")

# 폐포 출력 및 동치 관계 재판별
def print_closure(original, closure):

    print("변환 전:")
    print_matrix(original)

    print()

    print("변환 후:")
    print_matrix(closure)

    # 추가 기능
    print_added_pairs(original, closure)

    print()
    print("변환 후 관계 판별:")
    if is_equivalence(closure):
        print_equivalence_classes(closure)

# 행렬 출력
def print_matrix(matrix):
    for row in matrix:
        print(" ".join(map(str, row)))

# 메인 함수
def main():
    matrix = input_matrix()

    print("\n===== 입력된 관계 행렬 =====")
    print_matrix(matrix)

    print("\n===== 관계 판별 =====")
    if is_equivalence(matrix):
        print_equivalence_classes(matrix)
    else:
        if not is_reflexive(matrix):
            closure = reflexive_closure(matrix)
            print("===== 반사 폐포 =====")
            print_closure(matrix, closure)
            matrix = closure

        if not is_symmetric(matrix):
            closure = symmetric_closure(matrix)
            print("===== 대칭 폐포 =====")
            print_closure(matrix, closure)
            matrix = closure

        if not is_transitive(matrix):
            closure = transitive_closure(matrix)
            print("===== 추이 폐포 =====")
            print_closure(matrix, closure)
            matrix = closure

if __name__ == "__main__":
    main()


