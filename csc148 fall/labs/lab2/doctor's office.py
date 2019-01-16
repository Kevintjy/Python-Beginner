# Doctor's Office
# ===============
#
# A doctor's office needs software for scheduling appointments. It
# is a large practise with 10 to 15 doctors and several thousand
# patients. Patients can make an appointment with a doctor, and
# all appointments last 1 hour. Doctors schedule blocks of time
# when they are available for appointments. Each patient has a
# primary doctor. If their primary doctor is available on the hour
# and day when they wish to book they must see them; otherwise,
# they can see any doctor. A patient may cancel an appointment,
# but if they cancel more than 10, they are no longer allowed to
# book appointments (ever!). Doctors can cancel a block of time
# when they had said they were unavailable; any patients who had
# appointments during that block get rescheduled at the earliest
# possible time, regardless of which doctor they get.


class Schedule:
    def __init__(self):
        self.doctor = []
        self.patient = []

    def create_doctor(self, name):
        doc = Doctor(name)
        self.doctor.append(doc)
        return doc

    def create_patient(self, name, pri_doc):
        patient = Patient(name, pri_doc)
        self.patient.append(patient)
        return patient

    def patient_book(self, patient, year, month, day, time):
        if patient.cancel_num > 10:
            print(patient.name + ' is not allowed to book')
            return
        if patient.book(year, month, day, time): return
        for doc in self.doctor:
            for i in range(len(doc.available_time)):
                if doc.available_time[i][0] == (year, month, day) and \
                        time in doc.available_time[i][1]:
                    doc.available_time[i][1].remove(time)
                    patient.appoint.append([(year, month, day), time, doc.name])
                    return
        print('not available')

    def patient_cancel(self, patient, year, month, day, time, doc):
        if not ([(year, month, day), time, doc.name] in patient.appoint):
            print('you did not book this time')
            return
        patient.appoint.remove([(year, month, day), time, doc.name])
        for i in doc.available_time:
            if i[0] == (year, month, day):
                i[1].append(time)
        patient.cancel_num += 1


class Doctor:
    """
    the class of doctor
    """
    def __init__(self, name):
        self.name = name
        self.available_time = []

    def schedule(self, year, month, day, time_start, time_end):
        temp = [(year, month, day), [x for x in range(time_start, time_end)]]
        self.available_time.append(temp)

    def cancel(self, year, month, day, time_start, time_end):
        temp = [(year, month, day), [x for x in range(time_start, time_end)]]
        self.available_time.remove(temp)


class Patient:
    def __init__(self, name, pri_doc):
        self.name = name
        self.cancel_num = 0
        self.pri_doc = pri_doc
        self.appoint = []

    def book(self, year, month, day, time):
        if self.cancel_num > 10:
            print('you are not allowed to book')
            return
        for i in range(len(self.pri_doc.available_time)):
            if self.pri_doc.available_time[i][0] == (year, month, day) and\
                    time in self.pri_doc.available_time[i][1]:
                self.pri_doc.available_time[i][1].remove(time)
                self.appoint.append([(year, month, day), time, self.pri_doc.name])
                return True
        return False

    def cancel_num(self):
        return self.cancel_num


if __name__ == '__main__':
    s = Schedule()
    doc1 = s.create_doctor('doc1')
    doc2 = s.create_doctor('doc2')
    p1 = s.create_patient('p1', doc1)
    p2 = s.create_patient('p2', doc1)
    p3 = s.create_patient('p3', doc2)
    doc1.schedule(1,1,1,1,6)
    doc2.schedule(1,1,1,6,7)
    s.patient_book(p1,1,1,1,6)
    s.patient_cancel(p1,1,1,1,6,doc1)
    print(p1.appoint)
    print(doc2.available_time)
    print(p1.cancel_num)









