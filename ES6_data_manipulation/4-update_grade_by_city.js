export default function updateStudentGradeByCity(studentList, city, newGrades) {
    const students = studentList.filter((student) => student.location === city);
    const studentsWithGrades = students.map((student) => {
        const gradeObj = newGrades.find((gradeItem) => gradeItem.studentId === student.id);
        const grade = gradeObj ? gradeObj.grade : "N/A";
        return {
        ...student,
        grade: grade
    };
    });
    return studentsWithGrades;
}