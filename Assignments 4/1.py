def course_code():
    
        nhap_khoa_hoc = input(" Nhap khoa hoc vao cho bo: ")
        
        if nhap_khoa_hoc[:3].upper() and nhap_khoa_hoc[3:].isdigit() and nhap_khoa_hoc == 6:
            return " True "
        else :
            return " False "
    
    
print(course_code())
            
