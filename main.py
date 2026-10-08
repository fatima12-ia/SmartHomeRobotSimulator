import streamlit as st

st.set_page_config(
    page_title="Smart Home Robot Simulator",
    page_icon="🤖",
    layout="wide"
)

st.title("🤖 Smart Home Robot Simulator")
st.caption("AI-Based Intelligent Home Management System")
st.write(
    "An AI-based smart home simulation using "
    "Production Systems, Forward Reasoning and Backward Reasoning."
)

# Robot state
if "robot_location" not in st.session_state:
    st.session_state.robot_location = "Living Room"

if "battery" not in st.session_state:
    st.session_state.battery = 100

# House state
if "kitchen_dirty" not in st.session_state:
    st.session_state.kitchen_dirty = True

if "bathroom_dirty" not in st.session_state:
    st.session_state.bathroom_dirty = False

if "living_room_light" not in st.session_state:
    st.session_state.living_room_light = True

if "kitchen_light" not in st.session_state:
    st.session_state.kitchen_light = True

if "bedroom_light" not in st.session_state:
    st.session_state.bedroom_light = False

if "bathroom_light" not in st.session_state:
    st.session_state.bathroom_light = False

# Smart Home
st.subheader("🏠 Smart Home")

col1, col2 = st.columns(2)

with col1:
    st.info("🛋️ Living Room")
    st.write(
        "Light: " +
        ("ON" if st.session_state.living_room_light else "OFF")
    )
    st.write("Person: Present")

    st.info("🍳 Kitchen")
    st.write(
        "Condition: " +
        ("Dirty" if st.session_state.kitchen_dirty else "Clean")
    )
    st.write(
        "Light: " +
        ("ON" if st.session_state.kitchen_light else "OFF")
    )

with col2:
    st.info("🛏️ Bedroom")
    st.write(
        "Light: " +
        ("ON" if st.session_state.bedroom_light else "OFF")
    )
    st.write("Person: Absent")

    st.info("🚿 Bathroom")
    st.write(
        "Condition: " +
        ("Dirty" if st.session_state.bathroom_dirty else "Clean")
    )
    st.write(
        "Light: " +
        ("ON" if st.session_state.bathroom_light else "OFF")
    )

# Reasoning Mode
st.subheader("🧠 AI Reasoning Mode")

reasoning_mode = st.radio(
    "Choose the reasoning method:",
    ["Forward Reasoning", "Backward Reasoning"]
)

# Production Rules
st.subheader("📋 Production Rules")

rules = {
    "R1": "IF kitchen is dirty → THEN move to kitchen",
    "R2": "IF robot is in kitchen AND kitchen is dirty → THEN clean kitchen",
    "R3": "IF bathroom is dirty → THEN move to bathroom",
    "R4": "IF robot is in bathroom AND bathroom is dirty → THEN clean bathroom",
    "R5": "IF room is unoccupied AND light is ON → THEN turn OFF light",
    "R6": "IF all rooms are clean → THEN report house is clean"
}

for rule_id, rule in rules.items():
    st.write(f"**{rule_id}:** {rule}")

# Task
st.subheader("🎯 Select Robot Task")

task = st.selectbox(
    "Choose a task for the robot:",
    [
        "Clean the Kitchen",
        "Clean the Bathroom",
        "Turn Off Unnecessary Lights",
        "Check House Cleanliness"
    ]
)

# AI Simulation
if st.button("▶️ Start AI Simulation"):

    st.subheader("🧠 AI Reasoning Process")

    if reasoning_mode == "Forward Reasoning":

        if task == "Clean the Kitchen":

            if st.session_state.kitchen_dirty:

                st.write("🔹 Initial Fact: Kitchen is dirty.")

                st.write(
                    "🔹 Rule R1 activated: "
                    "Kitchen is dirty → Move to Kitchen."
                )

                st.write(
                    f"🤖 Robot moves from "
                    f"{st.session_state.robot_location} to Kitchen."
                )

                st.session_state.robot_location = "Kitchen"
                st.session_state.battery = max(
                    0,
                    st.session_state.battery - 10
                )

                st.write(
                    "🔹 New Fact: Robot is now in Kitchen."
                )

                st.write(
                    "🔹 Rule R2 activated: "
                    "Robot is in Kitchen AND Kitchen is dirty "
                    "→ Clean Kitchen."
                )

                st.write("🧹 Robot cleans the Kitchen.")

                st.session_state.kitchen_dirty = False

                st.success(
                    "✅ Kitchen is now clean. Goal achieved!"
                )

            else:
                st.info("ℹ️ Kitchen is already clean.")

        elif task == "Clean the Bathroom":

            if st.session_state.bathroom_dirty:

                st.write("🔹 Initial Fact: Bathroom is dirty.")

                st.write(
                    "🔹 Rule R3 activated: "
                    "Bathroom is dirty → Move to Bathroom."
                )

                st.write(
                    f"🤖 Robot moves from "
                    f"{st.session_state.robot_location} to Bathroom."
                )

                st.session_state.robot_location = "Bathroom"
                st.session_state.battery = max(
                    0,
                    st.session_state.battery - 10
                )

                st.write(
                    "🔹 New Fact: Robot is now in Bathroom."
                )

                st.write(
                    "🔹 Rule R4 activated: "
                    "Robot is in Bathroom AND Bathroom is dirty "
                    "→ Clean Bathroom."
                )

                st.write("🧹 Robot cleans the Bathroom.")

                st.session_state.bathroom_dirty = False

                st.success(
                    "✅ Bathroom is now clean. Goal achieved!"
                )

            else:
                st.info("ℹ️ Bathroom is already clean.")

        elif task == "Turn Off Unnecessary Lights":

            st.write(
                "🔹 AI checks the house for unnecessary lights."
            )

            action_taken = False

            if st.session_state.kitchen_light:
                st.write(
                    "🔹 Rule R5 activated: "
                    "Kitchen is unoccupied → Turn OFF light."
                )
                st.session_state.kitchen_light = False
                action_taken = True

            if st.session_state.bedroom_light:
                st.write(
                    "🔹 Rule R5 activated: "
                    "Bedroom is unoccupied → Turn OFF light."
                )
                st.session_state.bedroom_light = False
                action_taken = True

            if st.session_state.bathroom_light:
                st.write(
                    "🔹 Rule R5 activated: "
                    "Bathroom is unoccupied → Turn OFF light."
                )
                st.session_state.bathroom_light = False
                action_taken = True

            if action_taken:
                st.success(
                    "✅ Unnecessary lights have been turned OFF."
                )
            else:
                st.info(
                    "ℹ️ No unnecessary lights were found."
                )

        elif task == "Check House Cleanliness":

            st.write(
                "🔹 AI checks the cleanliness of all rooms."
            )

            if (
                not st.session_state.kitchen_dirty
                and not st.session_state.bathroom_dirty
            ):
                st.write(
                    "🔹 Rule R6 activated: All rooms are clean."
                )
                st.success("✅ House is clean!")
            else:
                st.warning(
                    "⚠️ House is not completely clean."
                )

    elif reasoning_mode == "Backward Reasoning":

        if task == "Clean the Kitchen":

            st.write("🎯 Goal: Kitchen must be clean.")

            st.write(
                "🔹 Rule R2 can achieve this goal."
            )

            st.write(
                "   Robot must be in Kitchen AND "
                "Kitchen must be dirty."
            )

            st.write(
                "🔹 Requirement: Robot must be in Kitchen."
            )

            st.write(
                "🔹 Rule R1 can achieve this:"
            )

            st.write(
                "   Kitchen is dirty → Move to Kitchen."
            )

            st.write(
                "🔹 Required Fact: Kitchen is dirty."
            )

            if st.session_state.kitchen_dirty:

                st.write("✅ Required fact found.")

                st.write(
                    "🤖 Plan generated: "
                    "Move to Kitchen → Clean Kitchen."
                )

                st.session_state.robot_location = "Kitchen"
                st.session_state.battery = max(
                    0,
                    st.session_state.battery - 10
                )

                st.session_state.kitchen_dirty = False

                st.success(
                    "✅ Goal achieved using Backward Reasoning!"
                )

            else:
                st.info("ℹ️ Kitchen is already clean.")

        elif task == "Clean the Bathroom":

            st.write("🎯 Goal: Bathroom must be clean.")

            st.write(
                "🔹 Rule R4 can achieve this goal."
            )

            st.write(
                "   Robot must be in Bathroom AND "
                "Bathroom must be dirty."
            )

            st.write(
                "🔹 Rule R3 can achieve this:"
            )

            st.write(
                "   Bathroom is dirty → Move to Bathroom."
            )

            if st.session_state.bathroom_dirty:

                st.write("✅ Required fact found.")

                st.write(
                    "🤖 Plan generated: "
                    "Move to Bathroom → Clean Bathroom."
                )

                st.session_state.robot_location = "Bathroom"
                st.session_state.battery = max(
                    0,
                    st.session_state.battery - 10
                )

                st.session_state.bathroom_dirty = False

                st.success(
                    "✅ Goal achieved using Backward Reasoning!"
                )

            else:
                st.info("ℹ️ Bathroom is already clean.")

        elif task == "Turn Off Unnecessary Lights":

            st.write(
                "🎯 Goal: Turn OFF unnecessary lights."
            )

            st.write(
                "🔹 Rule R5 is used to achieve this goal."
            )

            st.session_state.kitchen_light = False
            st.session_state.bedroom_light = False
            st.session_state.bathroom_light = False

            st.success(
                "✅ Unnecessary lights turned OFF."
            )

        elif task == "Check House Cleanliness":

            st.write(
                "🎯 Goal: Determine whether the entire house is clean."
            )

            st.write(
                "🔹 Rule R6 can achieve this goal."
            )

            if (
                not st.session_state.kitchen_dirty
                and not st.session_state.bathroom_dirty
            ):
                st.success(
                    "✅ Goal achieved: House is clean!"
                )
            else:
                st.warning(
                    "⚠️ Some rooms are still dirty."
                )

# Robot Status
st.subheader("🤖 Robot Status")

robot_col1, robot_col2, robot_col3 = st.columns(3)

with robot_col1:
    st.metric(
        "Location",
        st.session_state.robot_location
    )

with robot_col2:
    st.metric(
        "Battery",
        f"{st.session_state.battery}%"
    )

with robot_col3:
    st.metric(
        "Current Task",
        task
    )

# About
st.subheader("ℹ️ About the AI System")

st.write(
    "This simulator demonstrates how an intelligent robot "
    "uses Production Systems, Forward Reasoning and "
    "Backward Reasoning to make decisions in a smart home."
)
st.divider()

if st.button("🔄 Reset Simulation"):
    st.session_state.robot_location = "Living Room"
    st.session_state.battery = 100
    st.session_state.kitchen_dirty = True
    st.session_state.bathroom_dirty = False
    st.session_state.living_room_light = True
    st.session_state.kitchen_light = True
    st.session_state.bedroom_light = False
    st.session_state.bathroom_light = False
    st.rerun()
st.divider()

st.subheader("🎛️ Environment Controls")

control_col1, control_col2 = st.columns(2)

with control_col1:
    st.write("🏠 Room Conditions")

    kitchen_status = st.checkbox(
        "Kitchen is Dirty",
        value=st.session_state.kitchen_dirty
    )

    bathroom_status = st.checkbox(
        "Bathroom is Dirty",
        value=st.session_state.bathroom_dirty
    )

with control_col2:
    st.write("💡 Light Controls")

    kitchen_light_status = st.checkbox(
        "Kitchen Light ON",
        value=st.session_state.kitchen_light
    )

    bedroom_light_status = st.checkbox(
        "Bedroom Light ON",
        value=st.session_state.bedroom_light
    )

if st.button("💾 Apply Environment Changes"):
    st.session_state.kitchen_dirty = kitchen_status
    st.session_state.bathroom_dirty = bathroom_status
    st.session_state.kitchen_light = kitchen_light_status
    st.session_state.bedroom_light = bedroom_light_status

    st.success("✅ Environment updated successfully!")
    st.rerun()