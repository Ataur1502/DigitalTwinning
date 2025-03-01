// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract ExperimentsAssignment {
    enum Status { NotStarted, Pending, Completed }

    struct Experiment {
        string description;
        Status status;
    }

    mapping(string => Experiment[]) private studentExperiments; // rollNo => list of experiments

    event ExperimentAssigned(string rollNo, string description, Status status);
    event ExperimentUpdated(string rollNo, uint256 index, Status newStatus);

    // Assign a new experiment to a student
    function assignExperiment(string memory rollNo, string memory description) public {
        studentExperiments[rollNo].push(Experiment(description, Status.NotStarted));
        emit ExperimentAssigned(rollNo, description, Status.NotStarted);
    }

    // Update status of a student's experiment
    function updateExperimentStatus(string memory rollNo, uint256 index, Status newStatus) public {
        require(index < studentExperiments[rollNo].length, "Invalid experiment index");
        studentExperiments[rollNo][index].status = newStatus;
        emit ExperimentUpdated(rollNo, index, newStatus);
    }

    // Get all experiments for a student
    function getExperiments(string memory rollNo) public view returns (Experiment[] memory) {
        return studentExperiments[rollNo];
    }
}
