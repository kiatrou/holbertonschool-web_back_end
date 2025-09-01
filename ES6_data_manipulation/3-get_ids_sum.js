export default function getStudentIdsSum(studentList) {
    return studentList.reduce((accumulator, student) => {
        return accumulator + student.id;
    }, 0);
}
