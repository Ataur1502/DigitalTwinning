// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract ExperimentStorage {
    
    // Experiment structure
    struct Experiment {
        uint256 v1;
        uint256 v2;
        uint256 m1;
        uint256 m2;
        string status;
    }

    // Mapping Roll Number => List of Experiments
    mapping(string => Experiment[]) private experiments;

    // Event for logging experiments
    event ExperimentRecorded(string rollNo, uint256 v1, uint256 v2, uint256 m1, uint256 m2, string status);

    // Function to store experiment data
    function storeExperiment(
        string memory rollNo, 
        uint256 v1, 
        uint256 v2, 
        uint256 m1, 
        uint256 m2, 
        string memory status
    ) public {
        experiments[rollNo].push(Experiment(v1, v2, m1, m2, status));

        // Emit event
        emit ExperimentRecorded(rollNo, v1, v2, m1, m2, status);
    }

    // Function to retrieve all experiments of a student
    function getExperiments(string memory rollNo) public view returns (Experiment[] memory) {
        return experiments[rollNo];
    }
}
