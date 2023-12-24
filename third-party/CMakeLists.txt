cmake_minimum_required(VERSION 3.27)
# Define variables for the project and repository URL
set(PROJECT_NAME dbcppp)
set(REPO_URL https://github.com/xR3b0rn/dbcppp.git)

# Execute a command to clone the repository
execute_process(
    COMMAND git clone --recurse-submodules ${REPO_URL} ${CMAKE_BINARY_DIR}/external/${PROJECT_NAME}
    RESULT_VARIABLE clone_result
)

if(NOT ${clone_result} EQUAL 0)
    message(FATAL_ERROR "Failed to clone the repository.")
endif()

# Create a custom target that depends on the completion of the clone process
add_custom_target(${PROJECT_NAME}Clone
    DEPENDS ${CMAKE_BINARY_DIR}/external/${PROJECT_NAME}
)


add_subdirectory(${source_dir} ${CMAKE_BINARY_DIR}/external/YourProjectName-build)

# Enable CPack module
include(CPack)

# Set the basic CPack settings
set(CPACK_GENERATOR "NSIS")  # Use NSIS installer (you can use other generators as needed)
set(CPACK_PACKAGE_NAME "dbcppp")
set(CPACK_PACKAGE_VERSION "3.2.6")
set(CPACK_PACKAGE_FILE_NAME "${CPACK_PACKAGE_NAME}-${CPACK_PACKAGE_VERSION}")

# Specify files to be installed (your executable and any other necessary files)
install(TARGETS dbcppp DESTINATION bin)  # Replace YourExecutable with your actual target name

# Other installation instructions for additional files, if any

