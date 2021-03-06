import numpy as np
from .. import MsjROSBridgeProxy 
proxy = MsjROSBridgeProxy()

def test_msj_ros_bridge_proxy_reset():
    """reset function sets all joint angles to zero in simulation"""
    #assert "observation" in obs
    new_robot_state = proxy.forward_reset_command()
    assert np.allclose([0,0,0], new_robot_state.joint_angle)
    assert np.allclose([0,0,0], new_robot_state.joint_vel)

def test_msj_ros_bridge_proxy_step():
    """calling the step function changes the robot state"""

    random_action = [0.01, 0.01, 0.01, 0.015, 0.01, 0.02, 0.02, 0.02]
    initial_robot_state = proxy.forward_step_command(random_action)

    new_robot_state = proxy.forward_step_command(random_action)

    for x, y in zip(initial_robot_state.joint_angle, new_robot_state.joint_angle):
        assert np.abs(x - y) > 0.00001

    for x, y in zip(initial_robot_state.joint_vel, new_robot_state.joint_vel):
        assert ( np.abs(x - y) > 0.00001 or np.abs(x - y) == 0 )

def test_msj_ros_bridge_proxy_read_state():
    """calling the read state function doesn't change the robot state""" 

    initial_robot_state = proxy.read_state()
    new_robot_state = proxy.read_state()

    assert np.allclose(initial_robot_state.joint_angle, new_robot_state.joint_angle)
    assert np.allclose(initial_robot_state.joint_vel, new_robot_state.joint_vel)