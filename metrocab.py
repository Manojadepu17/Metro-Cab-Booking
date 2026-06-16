import streamlit as st
st.title("METRO + CAB BOOKING")
#METRO STATIONS LIST
STATIONS = [
    "LBNAGAR",
    "MALAKPET",
    "DILSUKHNAGAR",
    "KHAIRATABAD",
]
from_station=st.selectbox("From Station",STATIONS,index=None)
to_station=st.selectbox("To Station",STATIONS,index=None)
#number of tickets
tickets=st.number_input("Number of Tickets", min_value=1, max_value=10, value=1)
need_cab=st.radio("Do you need a cab?",
                  ["Yes", "No"], index=None,)
cab_destination=""
cab_fare=0
if need_cab=="Yes":
    cab_destination=st.text_input("Destination")
    cab_fare=130
if st.button("book now"):
    if from_station==to_station:
        st.error("From and To stations cannot be the same.")
    else:
        metro_fare=30*tickets
        total_fare=metro_fare+cab_fare
        st.success(f"Booking successful!")
        st.subheader("Booking Details:")
        st.write(f"From: {from_station}")
        st.write(f"To: {to_station}")
        st.write(f"Tickets: {tickets}")
        st.write(f"Cab Destination: {cab_destination}")
        st.write(f"Total Fare: ₹{total_fare}")
    if need_cab=="Yes":
        st.write(f"Cab From {to_station}")
        st.write(f"Cab To {cab_destination}")
        st.write(f"Cab Fare: ₹{cab_fare}")
        st.write(f"Total Fare: ₹{total_fare}")