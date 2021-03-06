import scipy
import main


def compute_global_error(g):
    """ Computes the total error of the graph"""
    Fx = 0

    # Loop over all edges
    for eid in g.edges:#= 1:length(g.edges)
        edge = g.edges(eid)

        # pose-pose constraint
        if edge.type == 'P':

            x1 = main.v2t(g.x[edge.fromIdx:edge.fromIdx+2])  # the first robot pose
            x2 = main.v2t(g.x[edge.toIdx:edge.toIdx+2])      # the second robot pose
      
            #TODO compute the error of the constraint and add it to Fx.
            # Use edge.measurement and edge.information to access the
            # measurement and the information matrix respectively.
      
        # pose-landmark constraint
        elif edge.type == 'L':
            x = g.x(edge.fromIdx:edge.fromIdx+2);  % the robot pose
            l = g.x(edge.toIdx:edge.toIdx+1);      % the landmark

            #TODO compute the error of the constraint and add it to Fx.
            # Use edge.measurement and edge.information to access the
            # measurement and the information matrix respectively.

    return Fx


def linearize_pose_landmark_constraint(x, l, z):
    """Compute the error of a pose-landmark constraint
    x 3x1 vector (x,y,theta) of the robot pose
    l 2x1 vector (x,y) of the landmark
    z 2x1 vector (x,y) of the measurement, the position of the landmark in
    the coordinate frame of the robot given by the vector x
    
    Output
    e 2x1 error of the constraint
    A 2x3 Jacobian wrt x
    B 2x2 Jacobian wrt l"""
    e = []
    A = []
    B = []
    # TODO compute the error and the Jacobians of the error
    
    
    return e, A, B


def linearize_pose_pose_constraint(x1, x2, z):
    """Compute the error of a pose-pose constraint
    x1 3x1 vector (x,y,theta) of the first robot pose
    x2 3x1 vector (x,y,theta) of the second robot pose
    z 3x1 vector (x,y,theta) of the measurement
    
    You may use the functions v2t() and t2v() to compute
    a Homogeneous matrix out of a (x, y, theta) vector
    for computing the error.
    
    Output
    e 3x1 error of the constraint
    A 3x3 Jacobian wrt x1
    B 3x3 Jacobian wrt x2"""
    
    # TODO compute the error and the Jacobians of the error
    
    return e, A, B


def linearize_and_solve(g):
    """ performs one iteration of the Gauss-Newton algorithm
    each constraint is linearized and added to the Hessian"""

    nnz = main.nnz_of_graph(g)

    # allocate the sparse H and the vector b
    H = spalloc(len(g.x), len(g.x), nnz) #u
    b = scipy.zeros((len(g.x), 1))

    needToAddPrior = True

    # compute the addend term to H and b for each of our constraints
    print('linearize and build system')
    for eid in xrange(len(g.edges)):# = 1:length(g.edges)
        edge = g.edges(eid)

        # pose-pose constraint
        if edge.type == 'P':#(strcmp(edge.type, 'P') != 0)
            # edge.fromIdx and edge.toIdx describe the location of
            # the first element of the pose in the state vector
            # You should use also this index when updating the elements
            # of the H matrix and the vector b.
            # edge.measurement is the measurement
            # edge.information is the information matrix
            x1 = g.x[edge.fromIdx:edge.fromIdx+2]  # the first robot pose
            x2 = g.x[edge.toIdx:edge.toIdx+2]      # the second robot pose
            
            # Computing the error and the Jacobians
            # e the error vector
            # A Jacobian wrt x1
            # B Jacobian wrt x2
            e, A, B = linearize_pose_pose_constraint(x1, x2, edge.measurement)


            # TODO: compute and add the term to H and b


            if needToAddPrior:
                # TODO: add the prior for one pose of this edge
                # This fixes one node to remain at its current location
      
                needToAddPrior = False

        # pose-landmark constraint
        elif edge.type = 'L':#(strcmp(edge.type, 'L') != 0)
            # edge.fromIdx and edge.toIdx describe the location of
            # the first element of the pose and the landmark in the state vector
            # You should use also this index when updating the elements
            # of the H matrix and the vector b.
            # edge.measurement is the measurement
            # edge.information is the information matrix
            x1 = g.x[edge.fromIdx:edge.fromIdx+2]  # the robot pose
            x2 = g.x[edge.toIdx:edge.toIdx+1]      # the landmark
          
            # Computing the error and the Jacobians
            # e the error vector
            # A Jacobian wrt x1
            # B Jacobian wrt x2
            [e, A, B] = linearize_pose_landmark_constraint(x1, x2, edge.measurement)


            # TODO: compute and add the term to H and b

    print('solving system');

    # TODO: solve the linear system, whereas the solution should be stored in dx
    # Remember to use the backslash operator instead of inverting H

    return dx



