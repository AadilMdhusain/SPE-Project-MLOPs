# Use a Maven base image for building the application with OpenJDK 11
FROM maven:3.8.3-openjdk-11 AS build

# Set working directory
WORKDIR /app

# Copy the pom.xml and source code
COPY pom.xml .
COPY src ./src

# Build the project using Maven
RUN mvn clean install

# Use OpenJDK 11 to run the application
FROM openjdk:11-jre-slim

# Set working directory
WORKDIR /app

# Copy the JAR file from the build image
COPY --from=build /app/target/ScientificCalculator1-1.0-SNAPSHOT.jar /app/scientific-calculator.jar

# Command to run the JAR file
CMD ["java", "-jar", "scientific-calculator.jar"]

